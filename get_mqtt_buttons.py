import time
import paho.mqtt.client as mqtt

_input_q = []

_client = mqtt.Client("MQTT_Button_Wrapper")

  _input_q.append([player,payload])


def on_message(client,userdata,message):

  print("Received "+message.topic+","+message.payload)

  if (message.topic == "jumbo_press"):

    # the payload should be in the form of x,y
    # to make the interface look the same, we're gonna make this a tuple
    # with: (x, y, "P")
    payload_str = message.payload
    payload_data = split(payload_str)
    print("payload: ", payload_data)
 
    # should eventually error check this to prevent crashes...
    x = int(payload_data[0])
    y = int(payload_data[1])
    action_type =  "P"
  
    _input_q.append(x,y,action_type)

###
def read():
    global _input_q

    if (len(_input_q) > 0):
      input = _input_q[0]
      del _input_q[0]
      return input
    else:
      return None
####

brokername = read_broker()
_client.on_message=on_message

try:
  _client.connect(brokername)
except:
  print("Unable to connect to MQTT broker: "+brokername)
  exit(0)

_client.loop_start()
    
_client.subscribe("jumbo_press");
