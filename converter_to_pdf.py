#convert images to pdf
from PIL import Image

#convert from png
def convert_png_to_pdf(path):
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    rgb_im.save(path.replace('png', 'pdf'))

#convert from jpg
def convert_jpg_to_pdf(path):
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    rgb_im.save(path.replace('jpg', 'pdf'))

#decomment the function you need
def main():
    print('--------------------------')
    path = str(input('Insert path of the image: '))
    #get the last 3 characters of the path
    var = path[-3:]
    print('Starting conversion...')
    print('--------------------------')
    if var == 'png':
        convert_png_to_pdf(path)
        print('Image converted successfully!')
        exit()
    elif var == 'jpg':
        convert_jpg_to_pdf(path)
        print('Image converted successfully!')
        exit()
    else:
        print('Extension not supported')
        main()

if __name__ == '__main__':
    main()
