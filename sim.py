import os
from PyPDF2 import PdfReader, PdfWriter

def find_phrases_and_create_new_pdf(input_pdf_path, output_pdf_path, start_phrase, end_phrase):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    start_page = None
    end_page = None

    # Find the start and end pages
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if start_page is None and start_phrase in text:
            start_page = page_number
        if start_page is not None and end_phrase in text:
            end_page = page_number
            break

    # Check if the start and end pages are identified
    if start_page is not None and end_page is not None:
        print(f"Phrase '{start_phrase}' found on page {start_page}")
        print(f"Phrase '{end_phrase}' found on page {end_page}")

        # Add the first page to the new PDF
        writer.add_page(reader.pages[0])  # Add the first page

        # Add pages from the start page to the end page (exclusive of end_page)
        for page in reader.pages[start_page-1:end_page]:  # Adjust to 0-based index
            writer.add_page(page)

        # Write to a new PDF
        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"New PDF created from page 1 and {start_page} to {end_page-1} at '{output_pdf_path}'")
    else:
        print("Phrases not found in the document.")

def process_directory(directory_path, start_phrase, end_phrase):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            input_pdf_path = os.path.join(directory_path, filename)
            output_pdf_path = os.path.join(directory_path, f"processed_{filename}")
            find_phrases_and_create_new_pdf(input_pdf_path, output_pdf_path, start_phrase, end_phrase)

# Specify the directory containing your PDF files
directory_path = "./filings/AMZN"
## AMAZON
start_phrase = "Report of Ernst & Young LLP"
end_phrase = "NOTES TO "

# Process all PDF files in the directory
process_directory(directory_path, start_phrase, end_phrase)
