# RAG SII EsSalud — Asistente Documental Inteligente

Implementación de **RAG (Retrieval-Augmented Generation)** para el proyecto **SII – Implementación de un ERP en EsSalud – La Libertad**, Módulo de Procesos de Soporte Administrativo y Prestaciones Económicas (Trámite Documentario / SISGEDO y Mesa de Partes Digital).

El sistema permite realizar consultas en lenguaje natural sobre la documentación del proyecto (procesos BPMN, requisitos funcionales y no funcionales, casos de uso, modelo de datos, marco normativo — Ley 29733, DS 016-2024-JUS, ISO 27001 — y metodología UWE), recuperando los fragmentos más relevantes mediante búsqueda semántica con embeddings y generando respuestas fundamentadas con Claude (API de Anthropic).

## Arquitectura

```
┌─────────────┐   1. carga    ┌──────────────┐   2. chunking   ┌───────────────┐
│  Corpus     │ ────────────► │   Ingesta    │ ──────────────► │  Embeddings   │
│ (.md/.docx) │               │ (ingest.py)  │                 │  (fastembed)  │
└─────────────┘               └──────────────┘                 └───────┬───────┘
                                                                       │ 3. indexado
                              ┌──────────────┐   5. contexto   ┌───────▼───────┐
   Pregunta del usuario ────► │  RAG Chain   │ ◄────────────── │   ChromaDB    │
                              │ (Claude API) │  4. búsqueda    │ (persistente) │
                              └──────┬───────┘     semántica   └───────────────┘
                                     │ 6. respuesta + fuentes citadas
                                     ▼
                        CLI (app.py)  /  API REST (FastAPI)
```

**Componentes:**

| Componente | Tecnología | Rol |
|---|---|---|
| Embeddings | `fastembed` — `paraphrase-multilingual-MiniLM-L12-v2` (ONNX) | Vectorización multilingüe (optimizada para español), sin GPU |
| Vector store | ChromaDB (persistente, distancia coseno) | Almacenamiento e indexado de chunks |
| Chunking | División por encabezados + párrafos, 900 caracteres con solapamiento de 150 | Preserva el contexto de cada sección del informe |
| LLM | Claude (`claude-sonnet-4-6`) vía API de Anthropic | Generación de respuestas fundamentadas en el contexto recuperado |
| Interfaz | CLI interactivo + API REST (FastAPI) | Consumo directo o integración con el ERP / Mesa de Partes Digital |

## Alineamiento con ISO/IEC 25059 (calidad de sistemas con IA)

Según lo propuesto en el informe del proyecto, el componente de IA cumple los atributos de calidad de la norma:

- **Explicabilidad**: cada respuesta incluye las fuentes recuperadas (documento, sección y puntaje de similitud), lo que permite auditar por qué el asistente respondió de determinada forma.
- **Robustez**: si la información no existe en el corpus, el asistente lo indica explícitamente en lugar de inventar; los errores de configuración (falta de API key, colección vacía) se manejan de forma controlada.
- **Adaptabilidad**: el corpus es extensible — basta con agregar nuevos documentos (`.md`, `.txt`, `.docx`) a `data/corpus/` y re-ejecutar la ingesta para que el conocimiento del asistente se actualice.

## Instalación

```bash
git clone <url-del-repo>
cd rag-sii-essalud

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env             # colocar tu ANTHROPIC_API_KEY
```

## Uso

### 1. Ingesta del corpus

Indexa todos los documentos de `data/corpus/` en ChromaDB:

```bash
python -m src.ingest           # ingesta incremental (upsert)
python -m src.ingest --reset   # recrear la colección desde cero
```

### 2. Chat interactivo (CLI)

```bash
python app.py
```

```
Tú > ¿Qué gestor de base de datos se eligió y por qué?

El proyecto seleccionó PostgreSQL como gestor de base de datos, debido a...

Fuentes consultadas:
  - SII_ESSALUD_Grupo1_V2_0.md > ELECCIÓN DEL GESTOR DE BASE DE DATOS (similitud 0.58)
```

Consulta única sin modo interactivo:

```bash
python app.py -q "¿Cómo funciona la firma digital en el trámite documentario?"
```

Solo recuperación semántica (sin llamar al LLM, no requiere API key):

```bash
python app.py --solo-buscar -q "requisitos de la mesa de partes digital"
```

### 3. API REST

```bash
uvicorn src.api:app --reload --port 8000
```

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/health` | Estado del servicio |
| `POST` | `/ask` | `{"question": "..."}` → respuesta RAG con fuentes |
| `POST` | `/search` | `{"question": "...", "k": 5}` → solo chunks recuperados |

Documentación interactiva (Swagger): `http://localhost:8000/docs`

### 4. Pruebas

Prueba de humo del pipeline (ingesta + recuperación, sin necesidad de API key):

```bash
python -m tests.test_retrieval
```

## Estructura del proyecto

```
rag-sii-essalud/
├── app.py                  # CLI interactivo
├── requirements.txt
├── .env.example            # plantilla de variables de entorno
├── data/
│   ├── corpus/             # documentos fuente (.md, .txt, .docx)
│   └── chroma_db/          # base vectorial persistente (git-ignored)
├── src/
│   ├── config.py           # configuración central (rutas, modelos, parámetros)
│   ├── embeddings.py       # función de embeddings (fastembed → ChromaDB)
│   ├── ingest.py           # pipeline de ingesta: carga → chunking → indexado
│   ├── retriever.py        # búsqueda semántica sobre ChromaDB
│   ├── rag_chain.py        # cadena RAG: recuperación + generación (Claude)
│   └── api.py              # API REST (FastAPI)
└── tests/
    └── test_retrieval.py   # pruebas de humo (no requieren API key)
```

## Configuración avanzada

Parámetros editables en `.env` (ver `.env.example`):

| Variable | Por defecto | Descripción |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Clave de la API de Anthropic (obligatoria para generación) |
| `LLM_MODEL` | `claude-sonnet-4-6` | Modelo de generación |
| `EMBEDDING_MODEL` | `paraphrase-multilingual-MiniLM-L12-v2` | Modelo de embeddings (fastembed) |
| `CHUNK_SIZE` | `900` | Tamaño de chunk en caracteres |
| `CHUNK_OVERLAP` | `150` | Solapamiento entre chunks |
| `TOP_K` | `5` | Chunks recuperados por consulta |

## Ampliar el corpus

1. Copiar los nuevos documentos (`.md`, `.txt` o `.docx`) a `data/corpus/`.
2. Ejecutar `python -m src.ingest`.
3. Listo — el asistente ya responde con el nuevo conocimiento.

---

**Curso:** Sistemas de Información Integrados — UPAO · NRC 5633 · Trujillo, 2026
**Grupo 1:** Lescano León · Medina Tirado · Mezones Burgos · Valverde Vásquez
