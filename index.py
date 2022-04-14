from PIL import Image, ImageOps
import os
from pillow_heif import register_heif_opener

max_width = 760
os.chdir('./images')
images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'heic', 'HEIC', 'JPEG'))]

# heic ext config
register_heif_opener()

print(images)
for image in images:
    # open file
    img = Image.open(image)
    # fix orientation
    img = ImageOps.exif_transpose(img)
    # resizing
    ratio = img.height / img.width
    if img.width > max_width:
      img = img.resize((max_width, int(max_width * ratio)), Image.Resampling.LANCZOS)
    # save, compress
    img.save("../compressed/c_"+image, optimize=True, quality=90)
             