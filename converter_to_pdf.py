#convert images to pdf
import os
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
    path = '/home/.../Pdf-works-utils/test/test_image.jpg'
    #convert_png_to_pdf(path)
    convert_jpg_to_pdf(path)

if __name__ == '__main__':
    main()
