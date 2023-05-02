#attach two pdf document
from PyPDF2 import PdfReader, PdfMerger
from io import BytesIO

#open first file
with open('/home/.../Pdf-works-utils/test/File_1.pdf', 'rb') as f:
    pdf1 = f.read()

#open second file
with open('/home/.../Pdf-works-utils/test/File_2.pdf', 'rb') as f:
    pdf2 = f.read()

#read and merge files
pdf1 = PdfReader(BytesIO(pdf1))
pdf2 = PdfReader(BytesIO(pdf2))

output = PdfMerger()

output.append(pdf1)
output.append(pdf2)

#save in the folder destination
with open('/home/.../Pdf-works-utils/test/output.pdf', 'wb') as f:
    output.write(f)

