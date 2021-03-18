import get_buttons.py

try:
  print("Press Ctl-C to stop")
  while True:
    button = get_button()

    if button != None:
      if button[2] == "P":
        print("Button Press. X="+str(button[0])+", Y="+str(button[1]))
      elif button[2] == "R":
        print("Button Relese. X="+str(button[0])+", Y="+str(button[1]))

except KeyboardInterrupt:
  sys.exit(0)
