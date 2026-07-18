"""
Recuperación semántica sobre la colección de ChromaDB.
"""
from dataclasses import dataclass
from typing import List

from .config import TOP_K
from .ingest import get_collection


@dataclass
class RetrievedChunk:
    text: str
    source: str
    section: str
    score: float  # similitud (1 - distancia coseno)


def retrieve(query: str, k: int = TOP_K) -> List[RetrievedChunk]:
    collection = get_collection()
    res = collection.query(query_texts=[query], n_results=k)
    chunks: List[RetrievedChunk] = []
    for doc, meta, dist in zip(
        res["documents"][0], res["metadatas"][0], res["distances"][0]
    ):
        chunks.append(
            RetrievedChunk(
                text=doc,
                source=meta.get("source", "?"),
                section=meta.get("section", "?"),
                score=round(1 - dist, 4),
            )
        )
    return chunks


def format_context(chunks: List[RetrievedChunk]) -> str:
    blocks = []
    for i, ch in enumerate(chunks, 1):
        blocks.append(
            f"--- Fragmento {i} (fuente: {ch.source} | sección: {ch.section} | similitud: {ch.score}) ---\n{ch.text}"
        )
    return "\n\n".join(blocks)
