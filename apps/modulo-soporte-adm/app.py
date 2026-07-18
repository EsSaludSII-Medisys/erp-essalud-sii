"""
CLI interactivo del asistente RAG - SII EsSalud.

Uso:
    python app.py                 # chat interactivo
    python app.py -q "pregunta"   # una sola consulta
    python app.py --solo-buscar -q "pregunta"   # solo recuperación (sin LLM)
"""
import argparse

from src.rag_chain import RAGChain
from src.retriever import format_context, retrieve

BANNER = """
================================================================
  Asistente RAG - SII EsSalud (Módulo de Soporte Administrativo)
  Escribe tu pregunta o 'salir' para terminar.
================================================================
"""


def print_result(result: dict) -> None:
    print("\n" + result["answer"])
    print("\nFuentes consultadas:")
    for s in result["sources"]:
        print(f"  - {s['source']} > {s['section']} (similitud {s['score']})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", help="Consulta única (modo no interactivo)")
    parser.add_argument(
        "--solo-buscar",
        action="store_true",
        help="Solo mostrar los chunks recuperados, sin llamar al LLM",
    )
    args = parser.parse_args()

    if args.solo_buscar:
        query = args.query or input("Consulta: ")
        print(format_context(retrieve(query)))
        return

    chain = RAGChain()

    if args.query:
        print_result(chain.ask(args.query))
        return

    print(BANNER)
    while True:
        try:
            question = input("\nTú > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question or question.lower() in {"salir", "exit", "quit"}:
            break
        print_result(chain.ask(question))


if __name__ == "__main__":
    main()
