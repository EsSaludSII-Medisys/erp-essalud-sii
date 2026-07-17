# Informe: Sistema de Búsqueda de Información en Documentos mediante RAG

**Trabajo individual**
**Autor:** Diego Jesús Medina Tirado
**Curso / Universidad:** Universidad Privada Antenor Orrego (UPAO)
**Fecha:** 3 de julio de 2026
**Repositorio con la solución:** _[pegar aquí el enlace de GitHub]_
`https://github.com/Medina-Tirado-Diego/rag-sii-upao`

---

## 1. Planteamiento del problema

La universidad requiere un programa que permita realizar **búsqueda de
información sobre documentos alojados en un repositorio**. El usuario debe poder
ingresar una pregunta en lenguaje natural, por ejemplo:

> *"Requisitos para reserva de matrícula"*

…y el sistema debe devolver información pertinente sobre ese tema, extraída de
los documentos oficiales (reglamentos, guías de trámites, etc.).

Como propuesta tecnológica para el **futuro producto software** se emplea la
técnica de Inteligencia Artificial denominada **RAG (Retrieval-Augmented
Generation)**.

---

## 2. ¿Qué es RAG? (Retrieval-Augmented Generation)

RAG es una técnica que combina un **motor de búsqueda semántica** con un **modelo
de lenguaje (LLM)**. En vez de que el modelo responda solo con su conocimiento
interno (lo que puede producir invenciones o "alucinaciones"), primero se
**recuperan** los fragmentos de documento más relevantes y luego se le pide al
LLM que **genere** la respuesta usando esa información como contexto.

Consta de dos fases:

1. **Recuperación (Retrieval):** la pregunta del usuario se transforma en un
   *embedding* (un vector numérico que representa su significado). Se compara
   ese vector con los de todos los fragmentos de documento almacenados en una
   base de datos vectorial y se seleccionan los más similares.
2. **Generación (Generation):** los fragmentos recuperados se insertan como
   *contexto* dentro del prompt que recibe el LLM, el cual redacta la respuesta
   final basándose únicamente en dicha información.

### Diagrama de la arquitectura

```
FASE DE INDEXACIÓN (una sola vez):
Documentos → Fragmentar (chunks) → Generar embeddings → Guardar en Vector DB

FASE DE CONSULTA (cada pregunta):
Pregunta del usuario → Embedding → Búsqueda por similitud → Chunks relevantes
                                                                   │
                              Chunks + Pregunta → LLM → Respuesta final
```

### ¿Por qué se eligió RAG? — Ventajas para el producto futuro

| Ventaja | Beneficio para la universidad |
|---|---|
| **Respuestas basadas en fuentes reales** | Reduce las "alucinaciones"; la información sale de los reglamentos oficiales. |
| **Actualizable sin reentrenar el modelo** | Basta con añadir/editar documentos y re-indexar; no hay costoso reentrenamiento. |
| **Trazabilidad** | El sistema indica de qué documento proviene la respuesta. |
| **Escalabilidad** | De 3 documentos de prueba se puede crecer a todo el reglamento institucional. |
| **Bajo costo / privacidad** | Corre 100% local (sin enviar datos a servicios externos ni pagar APIs). |

---

## 3. Arquitectura y stack tecnológico implementado

Solución **100% local y gratuita** (sin claves de API):

| Componente | Tecnología elegida | Rol |
|---|---|---|
| Orquestación del flujo RAG | **LangChain** | Conecta carga, fragmentación, embeddings, búsqueda y LLM. |
| Base de datos vectorial | **ChromaDB** | Almacena los embeddings y realiza la búsqueda por similitud (local, sin servidor). |
| Modelo de embeddings | **sentence-transformers** (`paraphrase-multilingual-MiniLM-L12-v2`) | Convierte texto en vectores; modelo multilingüe (español). |
| Modelo de lenguaje (LLM) | **Ollama** con `llama3.2` | Genera la respuesta final localmente. |
| Lenguaje | **Python 3.13** | Implementación de los scripts. |

---

## 4. Estructura del proyecto y archivos .PY

```
rag-sii-upao/
├── documentos/            # Repositorio de documentos de prueba (.txt)
│   ├── matricula.txt      #   Reglamento de matrícula (incluye reserva de matrícula)
│   ├── becas.txt          #   Reglamento de becas
│   └── tramites.txt       #   Guía de trámites del SII
├── ingest.py              # (.PY) Indexa los documentos en ChromaDB
├── query.py               # (.PY) Recibe la pregunta y genera la respuesta
├── requirements.txt       # Paquetes usados con versión
├── README.md              # Documentación de instalación y uso
└── INFORME.md             # Este documento
```

Los dos archivos `.py` que evidencian la propuesta son **`ingest.py`**
(indexación) y **`query.py`** (consulta). Su código completo se anexa en la
sección 8.

---

## 5. Prompts usados como apoyo en la generación del RAG

### 5.1. Prompt dado a la IA (Claude) para generar el código

> *"Construir un sistema RAG en Python donde hay documentos de la universidad
> (reglamentos, requisitos de matrícula, procedimientos). El usuario hace una
> pregunta en lenguaje natural (ej: '¿Cuáles son los requisitos para reserva de
> matrícula?') y el sistema busca en los documentos y devuelve una respuesta
> basada en esa información. Usar LangChain + ChromaDB. Embeddings locales con
> sentence-transformers y LLM local con Ollama (sin API keys). Crear `ingest.py`
> que carga los documentos, los fragmenta en chunks de 500 caracteres con
> solapamiento y los guarda en ChromaDB; y `query.py` que recupera los chunks
> más similares, arma un prompt con ellos como contexto y se lo pasa al LLM para
> la respuesta final. Preparar 2-3 documentos de prueba (matrícula, becas,
> trámites)."*

### 5.2. Prompt template interno del RAG (dentro de `query.py`)

Este es el prompt que el sistema construye automáticamente y envía al LLM en
cada consulta. Obliga al modelo a responder **solo** con el contexto recuperado:

```
SYSTEM:
Eres un asistente académico de la Universidad Privada Antenor Orrego (UPAO).
Responde la pregunta del estudiante ÚNICAMENTE con la información del CONTEXTO
proporcionado. Si la respuesta no está en el contexto, di claramente que no
cuentas con esa información. Responde en español, de forma clara y, cuando
corresponda, en forma de lista.

HUMAN:
CONTEXTO:
{contexto}

PREGUNTA: {pregunta}

RESPUESTA:
```

Donde `{contexto}` se reemplaza por los fragmentos recuperados de ChromaDB y
`{pregunta}` por la pregunta del usuario.

---

## 6. Paquetes usados (documentación de dependencias)

Instalados en un entorno virtual de Python. Versiones principales:

| Paquete | Versión |
|---|---|
| langchain | 1.3.11 |
| langchain-community | 0.4.2 |
| langchain-text-splitters | 1.1.2 |
| langchain-huggingface | 1.2.2 |
| langchain-chroma | 1.1.0 |
| langchain-ollama | 1.1.0 |
| chromadb | 1.5.9 |
| sentence-transformers | 5.6.0 |
| transformers | 5.13.0 |
| torch | 2.12.1+cpu |
| ollama | 0.6.2 |

> La lista completa y exacta está en el archivo `requirements.txt` (generado con
> `pip freeze`).

### Casos/problemas encontrados y su solución (documentados)

| Caso | Solución aplicada |
|---|---|
| `ModuleNotFoundError` al ejecutar los scripts | El intérprete `python` no apuntaba al entorno virtual; se recreó el `.venv` y se instalaron las dependencias en él. |
| Error `[Errno 28] No space left on device` al instalar | `torch` arrastra ~2.5 GB de librerías CUDA de NVIDIA que llenaban `/tmp`. Se instaló **torch CPU** (~192 MB) desde `https://download.pytorch.org/whl/cpu`, suficiente porque los embeddings corren en CPU. |
| `/tmp` demasiado pequeño durante la instalación | Se redirigió el temporal al disco principal con `TMPDIR=~/tmp-pip`. |
| Ollama no instalado | Se instaló como servicio del sistema y se descargó el modelo con `ollama pull llama3.2`. |

---

## 7. Ejecución y evidencia de funcionamiento

### Comandos

```bash
# 1) Indexar los documentos (crea la base vectorial)
python ingest.py

# 2) Realizar la consulta de ejemplo
python query.py "¿Cuáles son los requisitos para reserva de matrícula?"
```

### Salida real del programa (caso de ejemplo del enunciado)

```
=== PREGUNTA: ¿Cuáles son los requisitos para reserva de matrícula? ===

--- RESPUESTA ---
Según el Fragmento 3 y Fragmento 4, los requisitos para la reserva de
matrícula son:

* Solicitud dirigida al Director de la Escuela Profesional a través del
  sistema SII.
* No tener deudas pendientes con la universidad (pensiones, biblioteca,
  laboratorio).
* Haberse matriculado al menos en un semestre académico anterior.
* Pago de la tasa administrativa por reserva de matrícula vigente.
* La reserva se concede por un máximo de dos (2) semestres académicos
  consecutivos o alternos durante toda la carrera.

--- FUENTES CONSULTADAS ---
  * documentos/matricula.txt
  * documentos/matricula.txt
  * documentos/matricula.txt
  * documentos/matricula.txt
```

> **[Insertar aquí la captura de pantalla de la terminal con esta salida.]**

El sistema recuperó correctamente los fragmentos del documento `matricula.txt`
y el LLM generó una respuesta fiel a la fuente, sin inventar información.

---

## 8. Anexo: código fuente de los archivos .PY

### 8.1. `ingest.py` — Indexación

```python
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DOCS_DIR = Path("documentos")
CHROMA_DIR = "chroma_db"
COLLECTION = "reglamentos_upao"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def cargar_documentos():
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
```

### 8.2. `query.py` — Consulta

```python
import sys

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

CHROMA_DIR = "chroma_db"
COLLECTION = "reglamentos_upao"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "llama3.2"
TOP_K = 4

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


def _ejecutar(pregunta, retriever, llm):
    print(f"\n=== PREGUNTA: {pregunta} ===")
    respuesta, docs = responder(pregunta, retriever, llm)
    print("\n--- RESPUESTA ---")
    print(respuesta)
    print("\n--- FUENTES CONSULTADAS ---")
    for doc in docs:
        print(f"  * {doc.metadata.get('source', 'desconocida')}")
    print()


def main():
    retriever, llm = construir_cadena()
    if len(sys.argv) > 1:
        _ejecutar(" ".join(sys.argv[1:]), retriever, llm)
    else:
        print("Modo interactivo. Escribe tu pregunta (Ctrl+C para salir).\n")
        try:
            while True:
                pregunta = input("Pregunta> ").strip()
                if pregunta:
                    _ejecutar(pregunta, retriever, llm)
        except (KeyboardInterrupt, EOFError):
            print("\nHasta luego.")


if __name__ == "__main__":
    main()
```

---

## 9. Conclusión

Se implementó y se probó con éxito un sistema **RAG** que responde preguntas en
lenguaje natural sobre documentos de la universidad, funcionando de forma **local
y gratuita**. El caso de ejemplo del enunciado ("Requisitos para reserva de
matrícula") se resolvió correctamente, recuperando la información del reglamento
y generando una respuesta fiel a la fuente. Esta arquitectura constituye una base
sólida y escalable para el **futuro producto software** de la universidad,
pudiendo ampliarse a la totalidad de reglamentos y trámites institucionales.
```
