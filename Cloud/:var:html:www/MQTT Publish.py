#Importing libraries
import paho.mqtt.client as mqtt
import time
import ssl

#Defining functions that will enablig logging, displaying connection
#and disconnection messages
def on_log(client, userdata, level, buf):
	print("log: "+buf)

def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("connected")
	else:
		print("Bad Connection. Returned code ",rc)

def on_disconnect(client, userdata, flags, rc=0):
	print("Disconnected. Returned code "+str(rc))

#Recieving inputs from user
username = "PiNMAPmqtt"
password = "Christmas"
topic = "NMAP"
message = "go"

#Setting the broker address
broker_address="52.56.169.42"

#Using a unique client id
client = mqtt.Client("1234")

#Assigning the functions to events on the client
client.on_connect=on_connect
client.on_disconnect=on_disconnect
#uncomment to enable logging
# client.on_log=on_log

print("Connecting to broker ",broker_address)

#connecting to the broker using the certificate, username and password
client.username_pw_set(username, password=password)
client.tls_set(ca_certs="./ca.crt")
client.tls_insecure_set(True)

client.connect(broker_address, 8883, 60) #connect to broker
client.loop_start()

#publish to the user inputted topic with the inputted message
client.publish(topic, message)

#Disconnect before ending the script
client.loop_stop()
client.disconnect();
