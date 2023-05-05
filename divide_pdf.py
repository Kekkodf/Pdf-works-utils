from PyPDF2 import PdfReader, PdfWriter, PdfMerger

def divide_pdf(path, start, end):
    reader = PdfReader(path)
    writer = PdfWriter()
    if (start > end or start < 0 or end < 0) or (start > len(reader.pages) or end > len(reader.pages)):
        print('Error: start must be less than end and both must be greater than 0')
        main()
    for page in reader.pages[start:end]:
        writer.add_page(page)

    with open('/home/kdf/Scrivania/Pdf-works-utils/test/divided.pdf', 'wb') as f:
        writer.write(f)

def main():
    print('--------------------------')
    path = str(input('Insert path of the pdf: '))
    print('--------------------------')
    print('Dividing pdf...')
    start = int(input('Insert start page: '))
    end = int(input('Insert end page: '))
    divide_pdf(path, start, end)
    print('--------------------------')
    print('Pdf divided successfully!')

if __name__ == '__main__':
    main()
