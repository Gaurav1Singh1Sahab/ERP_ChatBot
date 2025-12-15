# Enterprise Chatbot RAG Project
 Wanted to create an enterprise level chatbot

 Folder Structure

 ERP_ChatBot/
│
├── .github/
│   └── workflows/
│       └── ci_cd.yml               # GitHub Actions pipeline
│
├── data/
│   ├── raw_pdfs/                   # Original PDF documents
│   ├── processed_json/             # Converted JSON files
│   └── embeddings_db/              # ChromaDB persistent folder
│
├── src/
│   ├── configs/
│   │   ├── config.yaml             # Project configurations
│   │   └── logging.conf            # Logging configuration
│   │
│   ├── utils/
│   │   ├── logger.py               # Logger wrapper
│   │   ├── pdf_loader.py           # Read/convert PDFs → text
│   │   ├── json_converter.py       # Convert text → JSON
│   │   └── metadata_generator.py   # Assign fake author/country
│   │
│   ├── vectorstore/
│   │   ├── embedder.py             # Embedding using Ollama/Instructor
│   │   └── chroma_handler.py       # Insert/search from ChromaDB
│   │
│   ├── llm/
│   │   ├── llm_setup.py            # Ollama LLM config
│   │   ├── chain_rag.py            # Retrieval-Augmented Generation chain
│   │   ├── guardrails_checker.py   # Guardrails validation before output
│   │   └── lora_training.py        # Extra: LoRA/QLoRA fine-tuning script
│   │
│   ├── api/
│   │   └── server.py               # FastAPI backend (recommended)
│   │
│   └── app/
│       └── streamlit_app.py        # Streamlit UI
│
├── tests/
│   ├── test_loader.py
│   ├── test_vectorstore.py
│   └── test_llm_pipeline.py
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── run.sh                          # Startup script (local run)

