"""
Función de embeddings para ChromaDB usando fastembed (ONNX).
Se usa un modelo multilingüe para obtener buena calidad semántica en español
sin requerir GPU ni PyTorch.
"""
from typing import List

from chromadb import Documents, EmbeddingFunction, Embeddings
from fastembed import TextEmbedding

from .config import EMBEDDING_MODEL


class FastEmbedFunction(EmbeddingFunction):
    """Adaptador de fastembed al protocolo EmbeddingFunction de ChromaDB."""

    def __init__(self, model_name: str = EMBEDDING_MODEL):
        self.model_name = model_name
        self._model = TextEmbedding(model_name=model_name)

    def __call__(self, input: Documents) -> Embeddings:
        return [emb.tolist() for emb in self._model.embed(list(input))]

    def name(self) -> str:  # requerido por versiones recientes de chromadb
        return f"fastembed::{self.model_name}"


def get_embedding_function() -> FastEmbedFunction:
    return FastEmbedFunction()
