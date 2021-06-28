# importing libraries

import sys
import os
from PIL import Image

# grab first and second argument

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check is new/ exists, if not create

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex,

for filename in os.listdir(image_folder):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')

  # convert images to png
  # save to the new folder

  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')
