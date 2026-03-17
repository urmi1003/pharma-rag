from sentence_transformers import SentenceTransformer
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter

# load embedding model
model = SentenceTransformer("BAAI/bge-small-en")

# load pdf
pdf_path = "data/drugs_medicine.pdf"
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += page.get_text()

# chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(full_text)

# create embeddings
embeddings = model.encode(chunks)

print("Total chunks:", len(chunks))
print("Embedding shape:", len(embeddings), len(embeddings[0]))