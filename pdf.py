import pdfkit

# Path to your HTML file
html_file = 'full-submission.html'

# Path to save the PDF file
pdf_file = 'output.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file)
