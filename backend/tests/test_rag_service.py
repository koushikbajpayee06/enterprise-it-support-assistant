from langchain_core.documents import Document
import asyncio

import pytest

from app.services import rag_service
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableLambda
from app.schemas.rag import Citation
from app.services.rag_service import (
    build_context_and_citations,
    select_used_citations,
)

from app.services.rag_service import (
    build_context_and_citations,
)


def test_build_context_and_citations() -> None:
    document_distance_pairs = [
        (
            Document(
                page_content=(
                    "LCEL uses the pipe operator to compose chains."
                ),
                metadata={
                    "source": "langchain-guide.pdf",
                    "page_number": 4,
                    "chunk_index": 3,
                },
            ),
            0.72,
        ),
        (
            Document(
                page_content=(
                    "Restart the VPN client before creating a ticket."
                ),
                metadata={
                    "source": "support-notes.txt",
                    "chunk_index": 1,
                },
            ),
            0.91,
        ),
    ]

    context, citations = build_context_and_citations(
        document_distance_pairs
    )

    assert "[1]" in context
    assert (
        "Source: langchain-guide.pdf, Page: 4, Chunk: 3"
        in context
    )
    assert (
        "LCEL uses the pipe operator to compose chains."
        in context
    )

    assert "[2]" in context
    assert (
        "Source: support-notes.txt, Chunk: 1"
        in context
    )

    assert len(citations) == 2

    assert citations[0].citation_id == 1
    assert citations[0].source == "langchain-guide.pdf"
    assert citations[0].page_number == 4
    assert citations[0].chunk_index == 3
    assert citations[0].distance == 0.72

    assert citations[1].citation_id == 2
    assert citations[1].source == "support-notes.txt"
    assert citations[1].page_number is None
    assert citations[1].chunk_index == 1
    assert citations[1].distance == 0.91


def test_generate_rag_answer_skips_llm_when_no_context(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        rag_service,
        "search_documents",
        lambda query, number_of_results: [],
    )

    def fail_if_model_is_called():
        raise AssertionError(
            "Chat model should not be called without context"
        )

    monkeypatch.setattr(
        rag_service,
        "get_chat_model",
        fail_if_model_is_called,
    )

    response = asyncio.run(
        rag_service.generate_rag_answer(
            question="How do I cook chicken biryani?",
            number_of_results=4,
        )
    )

    assert response.question == (
        "How do I cook chicken biryani?"
    )
    assert response.answer == (
        "I could not find relevant information "
        "in the indexed documents."
    )
    assert response.citations == []

def test_generate_rag_answer_uses_context_and_citations(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    retrieved_document = Document(
        page_content=(
            "LCEL is a declarative syntax for composing "
            "chains using the pipe operator."
        ),
        metadata={
            "source": "langchain-guide.pdf",
            "page_number": 4,
            "chunk_index": 3,
        },
    )

    monkeypatch.setattr(
        rag_service,
        "search_documents",
        lambda query, number_of_results: [
            (retrieved_document, 0.72)
        ],
    )

    captured_prompt = {}

    def fake_model_response(prompt):
        captured_prompt["value"] = prompt.to_string()

        return AIMessage(
            content=(
                "LCEL composes LangChain components "
                "using the pipe operator [1]."
            )
        )

    fake_model = RunnableLambda(fake_model_response)

    monkeypatch.setattr(
        rag_service,
        "get_chat_model",
        lambda: fake_model,
    )

    response = asyncio.run(
        rag_service.generate_rag_answer(
            question="What is LCEL?",
            number_of_results=4,
        )
    )

    assert response.question == "What is LCEL?"
    assert response.answer == (
        "LCEL composes LangChain components "
        "using the pipe operator [1]."
    )

    assert len(response.citations) == 1
    assert response.citations[0].citation_id == 1
    assert response.citations[0].source == (
        "langchain-guide.pdf"
    )
    assert response.citations[0].page_number == 4
    assert response.citations[0].distance == 0.72

    assert "What is LCEL?" in captured_prompt["value"]
    assert "langchain-guide.pdf" in captured_prompt["value"]
    assert "Page: 4" in captured_prompt["value"]
    assert (
        "LCEL is a declarative syntax"
        in captured_prompt["value"]
    )

def test_select_used_citations() -> None:
    citations = [
        Citation(
            citation_id=1,
            source="guide.pdf",
            page_number=17,
            chunk_index=23,
            content="LCEL cheat sheet",
            distance=0.74,
        ),
        Citation(
            citation_id=2,
            source="guide.pdf",
            page_number=17,
            chunk_index=25,
            content="Reference links",
            distance=0.77,
        ),
        Citation(
            citation_id=4,
            source="guide.pdf",
            page_number=4,
            chunk_index=4,
            content="LCEL uses the pipe operator.",
            distance=0.88,
        ),
    ]

    used_citations = select_used_citations(
        answer="LCEL uses the pipe operator [1][4].",
        citations=citations,
    )

    assert [
        citation.citation_id
        for citation in used_citations
    ] == [1, 4]