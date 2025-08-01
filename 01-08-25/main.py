import fitz  
import pdfplumber
import json

pdf_path = "main.pdf"
output_data = []

doc = fitz.open(pdf_path)

with pdfplumber.open(pdf_path) as plumber_pdf:

    for i in range(len(doc)):
        page_data = {}

        page = doc[i]
        text_blocks = page.get_text("text")  
        page_data["page"] = i + 1
        page_data["text"] = text_blocks.strip()

        plumber_page = plumber_pdf.pages[i]
        tables = plumber_page.extract_tables()
        extracted_tables = []

        for table in tables:
            extracted_tables.append(table) 

        page_data["tables"] = extracted_tables

       
        output_data.append(page_data)

with open("extracted_pdf_data.json", "w", encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4, ensure_ascii=False)

print("✅ PDF data successfully extracted to extracted_pdf_data.json")
