"""
Cadena RAG completa: recupera contexto de ChromaDB y genera la respuesta
con la API de Anthropic (Claude), manteniendo historial conversacional.
"""
from typing import Dict, List, Optional

from anthropic import Anthropic

from .config import ANTHROPIC_API_KEY, LLM_MODEL, MAX_TOKENS, SYSTEM_PROMPT, TOP_K
from .retriever import RetrievedChunk, format_context, retrieve


class RAGChain:
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or ANTHROPIC_API_KEY
        if not key:
            raise RuntimeError(
                "Falta ANTHROPIC_API_KEY. Copia .env.example a .env y coloca tu clave."
            )
        self.client = Anthropic(api_key=key)
        self.history: List[Dict[str, str]] = []

    def ask(self, question: str, k: int = TOP_K) -> Dict:
        chunks: List[RetrievedChunk] = retrieve(question, k=k)
        context = format_context(chunks)

        user_message = (
            f"CONTEXTO RECUPERADO DEL PROYECTO:\n{context}\n\n"
            f"PREGUNTA DEL USUARIO:\n{question}"
        )

        messages = self.history + [{"role": "user", "content": user_message}]

        response = self.client.messages.create(
            model=LLM_MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
        answer = "".join(b.text for b in response.content if b.type == "text")

        # Guardar en historial solo la pregunta limpia (sin el contexto inyectado)
        self.history.append({"role": "user", "content": question})
        self.history.append({"role": "assistant", "content": answer})
        # Limitar historial a los últimos 10 turnos
        self.history = self.history[-20:]

        return {
            "answer": answer,
            "sources": [
                {"source": c.source, "section": c.section, "score": c.score}
                for c in chunks
            ],
        }
