"""
ingest.py — Fase de indexación del RAG.

Carga los documentos de la carpeta ./documentos, los fragmenta en chunks,
genera embeddings locales con sentence-transformers y los guarda en una base
de datos vectorial ChromaDB persistente en ./chroma_db.

Uso:
    python ingest.py
"""

from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DOCS_DIR = Path("documentos")
CHROMA_DIR = "chroma_db"
COLLECTION = "reglamentos_upao"

# Modelo de embeddings local (gratis, se descarga la primera vez).
# Multilingüe y ligero: ideal para textos en español.
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def cargar_documentos():
    """Lee todos los .txt de la carpeta documentos/ como Documents de LangChain."""
    documentos = []
    for archivo in sorted(DOCS_DIR.glob("*.txt")):
        loader = TextLoader(str(archivo), encoding="utf-8")
        documentos.extend(loader.load())
        print(f"  - Cargado: {archivo.name}")
    return documentos


def main():
    print("1) Cargando documentos...")
    documentos = cargar_documentos()
    if not documentos:
        print("No se encontraron .txt en ./documentos. Aborta.")
        return

    print("2) Fragmentando en chunks (500 caracteres, overlap 100)...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documentos)
    print(f"   Total de chunks generados: {len(chunks)}")

    print("3) Generando embeddings locales (puede descargar el modelo)...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print("4) Guardando en ChromaDB...")
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION,
        persist_directory=CHROMA_DIR,
    )
    print(f"Listo. Base vectorial persistida en ./{CHROMA_DIR}")


if __name__ == "__main__":
    main()
