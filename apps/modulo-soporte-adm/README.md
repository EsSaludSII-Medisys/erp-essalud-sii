# RAG SII-UPAO — Asistente de reglamentos universitarios

Sistema **RAG (Retrieval-Augmented Generation)** que responde preguntas en
lenguaje natural sobre reglamentos y trámites de la UPAO (matrícula, becas,
trámites del SII), basándose en documentos reales en lugar del conocimiento
general del modelo.

Todo funciona **100% local y gratis**: embeddings con `sentence-transformers`,
base vectorial `ChromaDB` y el LLM con **Ollama** (sin API keys).

## ¿Qué es RAG y por qué se eligió?

RAG combina dos etapas:

1. **Recuperación (Retrieval):** la pregunta se convierte en un *embedding*
   (vector numérico) y se buscan por similitud los fragmentos de documento más
   parecidos en la base vectorial.
2. **Generación (Generation):** esos fragmentos se inyectan como *contexto* en
   el prompt del LLM, que redacta la respuesta final.

**Ventajas para el producto futuro:**
- **Respuestas basadas en fuentes reales** → menos alucinaciones.
- **Actualizable sin reentrenar:** basta con añadir/editar documentos y volver a
  ejecutar `ingest.py`.
- **Trazabilidad:** se muestran las fuentes consultadas.
- **Bajo costo:** corre en local, escalable luego a más documentos o a la nube.

## Arquitectura

```
Documentos → Fragmentar (chunks) → Embeddings → ChromaDB (Vector DB)
                                                        │
Pregunta usuario → Embedding → Búsqueda por similitud ─┘
                                                        │
                            Chunks + Pregunta → LLM (Ollama) → Respuesta
```

## Estructura

```
rag-sii-upao/
├── documentos/        # Reglamentos de prueba (.txt): matrícula, becas, trámites
├── ingest.py          # Indexa los documentos en ChromaDB
├── query.py           # Consulta el RAG y genera la respuesta con Ollama
├── requirements.txt
└── README.md
```

## Instalación

### 1. Entorno de Python y dependencias
```bash
python -m venv .venv
source .venv/bin/activate

# Instalar PRIMERO torch en su versión CPU (evita ~2.5 GB de CUDA de NVIDIA)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Luego el resto de dependencias
pip install -r requirements.txt
```
> **Nota importante:** por defecto `torch` arrastra ~2.5 GB de librerías CUDA de
> NVIDIA que pueden llenar `/tmp` y provocar el error *"No space left on device"*.
> Los embeddings de este proyecto corren en **CPU** y el LLM lo gestiona Ollama
> por separado, así que la versión CPU de torch (~192 MB) es suficiente.
> Si `/tmp` es pequeño, usa un temporal en tu disco:
> `mkdir -p ~/tmp-pip && TMPDIR=~/tmp-pip pip install -r requirements.txt`

### 2. Instalar Ollama y descargar un modelo
```bash
# Instalar Ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Descargar el modelo usado por defecto en query.py
ollama pull llama3.2
```
> Ollama debe estar corriendo (`ollama serve` o el servicio del sistema).

## Uso

```bash
# 1) Indexar los documentos (crea ./chroma_db)
python ingest.py

# 2) Preguntar (ejemplo del enunciado)
python query.py "¿Cuáles son los requisitos para reserva de matrícula?"

# Modo interactivo
python query.py
```

## Prompt template interno del RAG

Definido en `query.py`, obliga al modelo a responder **solo** con el contexto
recuperado:

```
system: Eres un asistente académico de la UPAO. Responde ÚNICAMENTE con la
        información del CONTEXTO. Si no está en el contexto, dilo claramente.
human:  CONTEXTO:
        {contexto}

        PREGUNTA: {pregunta}
        RESPUESTA:
```

## Notas de configuración
- Modelo de embeddings: `paraphrase-multilingual-MiniLM-L12-v2` (multilingüe).
- LLM por defecto: `llama3.2` (editable en `query.py`, variable `LLM_MODEL`).
- Chunks: 500 caracteres con 100 de solapamiento; `TOP_K = 4` fragmentos.
