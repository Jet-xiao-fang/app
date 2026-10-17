import os

MILVUS_URI = os.getenv("MILVUS_URI", "./milvus_requirements.db")

COLLECTION_NAME = "requirements_rag"

EMBEDDING_MODEL = "BAAI/bge-m3"
RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"
DENSE_DIM = 1024

MAX_CHARS = 600
OVERLAP = 100
TOP_K = 50
RERANK_TOP_N = 5
