from PyPDF2 import PdfFileMerger

pdfs = ['main.pdf', 'appendix1.pdf', 'appendix3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("LabProjectReport.pdf")
merger.close()