#attach two pdf document
from PyPDF2 import PdfReader, PdfMerger
from io import BytesIO


def attach_pdf(n, array_path):
    if n < 2:
        print('Error: you must attach at least two pdf')
        main()
    elif n!= len(array_path):
        print('Error: you must insert the same number of path and pdf')
        main()
    else:
        output = PdfMerger()
        for i in range(n):
            with open(array_path[i], 'rb') as f:
                pdf = f.read()
            pdf = PdfReader(BytesIO(pdf))
            output.append(pdf)
        with open('/home/kdf/Scrivania/Pdf-works-utils/test/Merged.pdf', 'wb') as f:
            output.write(f)

def main():
    print('--------------------------')
    n = int(input('Insert number of pdf to attach: '))
    print('--------------------------')
    array_path = []
    for i in range(n):
        path = str(input('Insert path of the pdf: '))
        array_path.append(path)
    print('--------------------------')
    print('Attaching pdf...')
    attach_pdf(n, array_path)
    print('--------------------------')
    print('Pdf attached successfully!')

if __name__ == '__main__':
    main()
