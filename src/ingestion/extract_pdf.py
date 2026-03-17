import fitz

pdf_path = "data/drugs_medicine.pdf"

doc = fitz.open(pdf_path)

full_text = ""

# loop through all pages
for page in doc:
    full_text += page.get_text()

print("Total characters:", len(full_text))