from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz

# load pdf again
pdf_path = "data/drugs_medicine.pdf"
doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

# create splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(full_text)

print("Total chunks:", len(chunks))
print("\nSample chunk:\n")
print(chunks[0])