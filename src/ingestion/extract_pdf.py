import fitz

# PDF path
pdf_path = "data/drugs_medicine.pdf"

# open PDF
doc = fitz.open(pdf_path)

# print total pages
print("Total pages:", len(doc))

# read first page
page = doc.load_page(0)
text = page.get_text()

print("\nFirst page text:\n")
print(text[:500])  # print first 500 characters