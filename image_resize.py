import os
from PIL import Image

SHOW_IMAGES = False

IMAGE_NAME = "vector_database/king_queen.png"
BASE_FOLDER = r"D:\dev\python\blog\content\images"

image_file = os.path.join(BASE_FOLDER, IMAGE_NAME)
img = Image.open(image_file)

if SHOW_IMAGES:
  img.show()

print(f'Source size {img.size}')

def shrink_image(im):
    base_height = 270
    wpercent = (base_height / float(im.size[1]))
    wsize = int((float(im.size[0]) * float(wpercent)))
    im = im.resize((wsize, base_height), Image.ANTIALIAS)
    return im
    # img.save('resized_image.jpg')

shrunk = shrink_image(img)
shrunk.show()

shrunk.save(image_file + '.res.png')
