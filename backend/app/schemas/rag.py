from pydantic import BaseModel, Field


class RagRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=2000,
    )
    number_of_results: int = Field(
        default=4,
        ge=1,
        le=10,
    )

class Citation(BaseModel):
    citation_id: int
    source: str
    page_number: int | None = None
    chunk_index: int
    content: str
    distance: float

class RagResponse(BaseModel):
    question: str
    answer: str
    citations: list[Citation]