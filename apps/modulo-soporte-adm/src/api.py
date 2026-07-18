"""
API REST del asistente RAG (FastAPI).
Permite integrar el asistente al ERP (p. ej. desde el frontend de la
Mesa de Partes Digital o SISGEDO).

Ejecución:
    uvicorn src.api:app --reload --port 8000

Endpoints:
    GET  /health         -> estado del servicio
    POST /ask            -> {"question": "..."}  respuesta RAG completa
    POST /search         -> {"question": "...", "k": 5}  solo recuperación
"""
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .rag_chain import RAGChain
from .retriever import retrieve

app = FastAPI(
    title="RAG SII EsSalud",
    description="Asistente documental del Módulo de Soporte Administrativo (SISGEDO / MPD)",
    version="1.0.0",
)

_chain: Optional[RAGChain] = None


def get_chain() -> RAGChain:
    global _chain
    if _chain is None:
        _chain = RAGChain()
    return _chain


class AskRequest(BaseModel):
    question: str


class SearchRequest(BaseModel):
    question: str
    k: int = 5


class Source(BaseModel):
    source: str
    section: str
    score: float


class AskResponse(BaseModel):
    answer: str
    sources: List[Source]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        return get_chain().ask(req.question)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search")
def search(req: SearchRequest):
    chunks = retrieve(req.question, k=req.k)
    return [
        {"text": c.text, "source": c.source, "section": c.section, "score": c.score}
        for c in chunks
    ]
