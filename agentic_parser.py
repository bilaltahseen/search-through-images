from agentic_doc.parse import parse_documents
from chromadb_client import add_to_chroma, search_chroma

# Parse an image and return the extracted data as markdown
def parse_image(image_path):
    results = parse_documents([image_path])
    parsed_doc = results[0]
    return parsed_doc.markdown

def parse_image_and_add_to_chroma(image_path):
    markdown_text = parse_image(image_path)
    add_to_chroma(markdown_text, image_path)