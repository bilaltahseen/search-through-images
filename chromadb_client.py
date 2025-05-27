import chromadb
import uuid
import os

CHROMA_DB_PATH = "chroma_db"
os.makedirs(CHROMA_DB_PATH, exist_ok=True)
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

collection = None
if not chroma_client.get_or_create_collection("rag-process"):
    collection = chroma_client.create_collection("rag-process")
else:
    collection = chroma_client.get_or_create_collection("rag-process")


def add_to_chroma(markdown_text, image_path):
    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[markdown_text],
        metadatas=[{"source": image_path}],
    )


def search_chroma(query):
    results = collection.query(
        query_texts=[query],
        n_results=1,
    )
    return results

