"""
Configuración central del sistema RAG - SII EsSalud.
Todas las rutas y parámetros se controlan desde aquí o vía variables de entorno (.env).
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# --- Rutas ---
BASE_DIR = Path(__file__).resolve().parent.parent
CORPUS_DIR = BASE_DIR / "data" / "corpus"
CHROMA_DIR = BASE_DIR / "data" / "chroma_db"

# --- Base vectorial ---
COLLECTION_NAME = "sii_essalud_docs"

# --- Embeddings (modelo multilingüe, funciona bien en español) ---
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
)

# --- Chunking ---
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "900"))       # caracteres por chunk
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))  # solapamiento entre chunks

# --- Recuperación ---
TOP_K = int(os.getenv("TOP_K", "5"))  # nro. de chunks recuperados por consulta

# --- LLM (Anthropic) ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))

SYSTEM_PROMPT = """Eres un asistente experto en el proyecto "SII - Implementación de un ERP en EsSalud - La Libertad",
específicamente en el Módulo de Procesos de Soporte Administrativo y Prestaciones Económicas
(Trámite Documentario / SISGEDO y Mesa de Partes Digital).

Responde SIEMPRE en español, de forma clara y precisa, usando ÚNICAMENTE la información
proporcionada en el contexto recuperado. Si la respuesta no está en el contexto, indícalo
honestamente y sugiere reformular la pregunta. Cita la sección del documento cuando sea posible
(por ejemplo: "según la sección REQUISITOS...").
"""
