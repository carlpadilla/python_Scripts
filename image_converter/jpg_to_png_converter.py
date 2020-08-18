import sys
import os
from PIL import Image

# example python3 jpg_to_png_converter.py ./pokedex ./new


# grab first and second args
image_directory = sys.argv[1]
output_directory = sys.argv[2]

# check if new exist, if not create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# iterate over image directory
for filename in os.listdir(image_directory):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_directory}{filename}')
    # converts images to png
    img.save(f'{output_directory}{clean_name}.png', 'png')
    # save to new folder

    print('all done.')


