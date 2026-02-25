import os
from PIL import Image

SHOW_IMAGES = False

IMAGE_NAME = os.path.join('change_seams', 'roboreplace.png')
BASE_FOLDER = os.path.join('content', 'images')

image_file = os.path.join(BASE_FOLDER, IMAGE_NAME)
img = Image.open(image_file)

if SHOW_IMAGES:
  img.show()

print(f'Source size {img.size}')

def shrink_image(im):
    base_height = 270
    wpercent = (base_height / float(im.size[1]))
    wsize = int((float(im.size[0]) * float(wpercent)))
    im = im.resize((wsize, base_height), Image.LANCZOS)
    return im

shrunk = shrink_image(img)
shrunk.show()

shrunk.save(image_file + '.res.jpg')
