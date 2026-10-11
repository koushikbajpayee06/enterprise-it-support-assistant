import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas.rag import RagRequest, RagResponse
from app.services.rag_service import generate_rag_answer


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/rag",
    tags=["RAG"],
)


@router.post(
    "/answer",
    response_model=RagResponse,
)
async def answer_question(
    request: RagRequest,
) -> RagResponse:
    try:
        return await generate_rag_answer(
            question=request.question,
            number_of_results=request.number_of_results,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except Exception as error:
        logger.exception(
            "Unexpected error while generating RAG answer"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate answer",
        ) from error