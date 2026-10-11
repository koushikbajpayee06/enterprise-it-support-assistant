from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.documents import router as documents_router

from app.api.routes.health import router as health_router
from app.config import settings

from app.api.routes.search import router as search_router
from app.api.routes.rag import router as rag_router
app = FastAPI(
    title="DocuMind AI API",
    description="Backend API for the DocuMind AI document intelligence platform.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(documents_router)
app.include_router(search_router)
app.include_router(rag_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to DocuMind AI API",
        "docs": "/docs",
    }