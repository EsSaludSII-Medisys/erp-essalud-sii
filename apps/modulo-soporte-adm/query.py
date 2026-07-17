"""
query.py — Fase de consulta del RAG.

Recibe una pregunta en lenguaje natural, recupera los chunks más relevantes
desde ChromaDB (búsqueda por similitud de embeddings) y los pasa como contexto
a un LLM local servido por Ollama para generar la respuesta final.

Uso:
    python query.py "¿Cuáles son los requisitos para reserva de matrícula?"
    python query.py          # modo interactivo
"""

import sys

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

CHROMA_DIR = "chroma_db"
COLLECTION = "reglamentos_upao"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "llama3.2"  # modelo servido por Ollama; cámbialo si usas otro
TOP_K = 4               # número de chunks a recuperar

# Prompt template interno del RAG: instruye al modelo a responder SOLO con el
# contexto recuperado, evitando alucinaciones.
PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "Eres un asistente académico de la Universidad Privada Antenor Orrego (UPAO). "
     "Responde la pregunta del estudiante ÚNICAMENTE con la información del "
     "CONTEXTO proporcionado. Si la respuesta no está en el contexto, di "
     "claramente que no cuentas con esa información. Responde en español, de "
     "forma clara y, cuando corresponda, en forma de lista."),
    ("human",
     "CONTEXTO:\n{contexto}\n\nPREGUNTA: {pregunta}\n\nRESPUESTA:"),
])


def formatear_contexto(docs):
    """Une los chunks recuperados en un solo bloque de texto con su fuente."""
    partes = []
    for i, doc in enumerate(docs, 1):
        fuente = doc.metadata.get("source", "desconocida")
        partes.append(f"[Fragmento {i} — fuente: {fuente}]\n{doc.page_content}")
    return "\n\n".join(partes)


def construir_cadena():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma(
        collection_name=COLLECTION,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})
    llm = ChatOllama(model=LLM_MODEL, temperature=0)
    return retriever, llm


def responder(pregunta, retriever, llm):
    docs = retriever.invoke(pregunta)
    contexto = formatear_contexto(docs)
    cadena = PROMPT | llm | StrOutputParser()
    respuesta = cadena.invoke({"contexto": contexto, "pregunta": pregunta})
    return respuesta, docs


def main():
    retriever, llm = construir_cadena()

    if len(sys.argv) > 1:
        preguntas = [" ".join(sys.argv[1:])]
    else:
        print("Modo interactivo. Escribe tu pregunta (Ctrl+C para salir).\n")
        preguntas = None

    if preguntas:
        for pregunta in preguntas:
            _ejecutar(pregunta, retriever, llm)
    else:
        try:
            while True:
                pregunta = input("Pregunta> ").strip()
                if pregunta:
                    _ejecutar(pregunta, retriever, llm)
        except (KeyboardInterrupt, EOFError):
            print("\nHasta luego.")


def _ejecutar(pregunta, retriever, llm):
    print(f"\n=== PREGUNTA: {pregunta} ===")
    respuesta, docs = responder(pregunta, retriever, llm)
    print("\n--- RESPUESTA ---")
    print(respuesta)
    print("\n--- FUENTES CONSULTADAS ---")
    for doc in docs:
        print(f"  * {doc.metadata.get('source', 'desconocida')}")
    print()


if __name__ == "__main__":
    main()
