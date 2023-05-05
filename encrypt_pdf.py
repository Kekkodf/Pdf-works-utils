from PyPDF2 import PdfReader, PdfWriter

#get pages using len(reader.pages)
def get_number_of_pages(path):
    reader = PdfReader(path)
    return len(reader.pages)

#split pdf
def encrypt_pdf(path, password):
    print('--------------------------')
    print('Encrypting pdf...')
    reader = PdfReader(path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)
    with open('/home/kdf/Scrivania/Pdf-works-utils/test/encrypted.pdf', 'wb') as f:
        writer.write(f)
    print('--------------------------')
    print('Pdf encrypted successfully!')
    print('--------------------------')

def main():
    path = str(input('Insert path of the pdf: '))
    password = str(input('Insert password for the encryption: '))
    encrypt_pdf(path, password)
    with open('/home/kdf/Scrivania/Pdf-works-utils/test/password.txt', 'wb') as f:
        f.write(password.encode())
    print('Password saved in password.txt')

if __name__ == '__main__':
    main()