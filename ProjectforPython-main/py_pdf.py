import PyPDF2

def Merging_PDF(pdfs,output):
    pdfmerge = PyPDF2.PdfMerger()

    for pdf in pdfs:
        pdfmerge.append(pdf)


    with open(output,'wb') as f:
        pdfmerge.write(f)



pdfs = ["harticket.pdf","InsertingArray-96.pdf"]


output = "linear-Insertingarray.pdf"

Merging_PDF(pdfs,output)


