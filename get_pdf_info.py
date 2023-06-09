from PyPDF2 import PdfReader

def main():
    path = str(input('Insert path of the pdf: '))
    with open(path, 'rb') as f:
        pdf = f.read()
    reader = PdfReader(path)

    meta = reader.metadata
    print('Number of pages: ', len(reader.pages))
    print('Author: ', meta.author)
    print('Creator: ', meta.creator)
    print('Producer: ', meta.producer)
    print('Subject: ', meta.subject)
    print('Title: ', meta.title)


if __name__ == '__main__':
    main()
