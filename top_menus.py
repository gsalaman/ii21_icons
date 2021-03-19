import time 
from datetime import datetime
import serial
#import get_buttons

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# this is the size of ONE of our matrixes. 
matrix_rows = 32 
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 8 
matrix_vertical = 2

total_rows = 128 
total_columns = 128

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular' 
options.pixel_mapper_config = 'U-mapper'

matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################
seconds_per_screen = 1

blank_screen = Image.new("RGB", (total_columns,total_rows))
home1 = Image.open("top/Homescreen.gif01.gif").convert("RGB")
home2 = Image.open("top/Homescreen.gif02.gif").convert("RGB")
home_images = (home1, home2)
num_home_images = len(home_images)
home_image_index = 0

matrix.SetImage(home_images[home_image_index],0,0)

try:
  print("Press CTRL-C to stop")
  last_update_time = datetime.now()

  while True:
    ''' 
    my_button = get_buttons.read()
    if my_button != None:
      # This is where we'd go to the next screen....but right now, we'll exit.
      exit(0)
    ''' 

    current_time = datetime.now()
    deltaT = current_time - last_update_time
 
    # check to see if it's time to switch the animated gif
    if deltaT.total_seconds() > seconds_per_screen:
      home_image_index = (home_image_index + 1) % num_home_images
      matrix.SetImage(home_images[home_image_index],0,0)
      last_update_time = current_time
    
    time.sleep(0.01)


except KeyboardInterrupt:
  exit(0)

