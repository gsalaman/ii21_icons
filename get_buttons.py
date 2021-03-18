import serial
import time

def get_button():
  global ser

  if ser.inWaiting() == 0:
    return None
  
  line = ser.readline()

  # first character for a press is "P"
  if (line[0] == 'P'):
    print("Press!")
    #now, we want two numbers separated by comma.
    line = line.strip("P\n\r ")
    button = line.split(",")
  
    # first check...do we have the right number of chars?
    if len(line) != 3:
      print("not text we care about")
      return None

    # a little check:  the two numbers should be between 0 and 7.
    # fix this:  non int's will crash.  want more robust.
    x_button = int(line[0])
    y_button = int(line[2])
    
    if ((x_button > 7) or (x_button < 0)):
      print("bad x")
      return None
  
    if ((y_button > 7) or (y_button < 0)):
      print("bad y")
      return None
   
    return(x_button,y_button)
    

  # first character for a release is "R"
  elif (line[0] == 'R'):
    print("Release!")

  else:
    print("Unexpected serial command:" + line)

  ser.flushInput() 

print("running")
ser = serial.Serial("/dev/tty.usbserial-DN02Z5R6", 9600, timeout=1) 
time.sleep(0.01) # wait for serial port to open.
if ser.isOpen():
  print("connected!")

  while True:
    my_button = get_button()
    if my_button != None:
      print("Main - button x: "+str(my_button[0]))
      print("Main - button y: "+str(my_button[1]))

    time.sleep(0.01)



