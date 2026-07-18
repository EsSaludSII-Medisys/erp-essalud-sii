"""
Pruebas de humo del pipeline de ingesta y recuperación.
No requieren ANTHROPIC_API_KEY (no llaman al LLM).

Ejecución:  python -m pytest tests/ -v   (o)   python -m tests.test_retrieval
"""
from src.ingest import ingest_corpus
from src.retriever import retrieve


def test_ingesta_y_recuperacion():
    total = ingest_corpus(reset=True)
    assert total > 0, "La ingesta no generó chunks"

    consultas = [
        "¿Cuál es el objetivo general del proyecto?",
        "¿Qué requisitos funcionales tiene la Mesa de Partes Digital?",
        "¿Qué gestor de base de datos se eligió y por qué?",
        "¿Cómo funciona la firma digital en el trámite documentario?",
    ]
    for q in consultas:
        chunks = retrieve(q, k=3)
        assert len(chunks) == 3
        assert all(c.score > 0 for c in chunks)
        print(f"\nQ: {q}")
        for c in chunks:
            print(f"   [{c.score}] {c.section} :: {c.text[:90].replace(chr(10),' ')}...")


if __name__ == "__main__":
    test_ingesta_y_recuperacion()
    print("\n[✓] Todas las pruebas pasaron")
