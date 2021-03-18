from time import sleep
import datetime

import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# this is the size of ONE of our matrixes. 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular' 

matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################
background = Image.open("andr_small.jpeg").convert("RGB")
background = background.resize((total_columns,total_rows))

matrix.SetImage(background,0,0)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(.1)

except KeyboardInterrupt:
  exit(0)

