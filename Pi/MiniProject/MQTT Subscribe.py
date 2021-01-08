#Importing libraries
import paho.mqtt.client as mqtt
import time
import ssl
import subprocess
import random
import string


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Defining functions that will enablig logging, displaying connection
#and disconnection messages, and what to do when recieving a message
def on_log(client, userdata, level, buf):
	print("log: "+buf)

def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("connected\n")
	else:
		print("Bad Connection. Returned code ",rc)

def on_disconnect(client, userdata, flags, rc=0):
	print("Disconnected. Returned code "+str(rc))

def on_message(client, userdata, msg):
	topic=msg.topic
	m_decode=str(msg.payload.decode("utf-8","ignore"))
	print("New Publish: ", m_decode)
	if m_decode == "go":
		# done = True
		subprocess.call(['./Copy.sh'])

#Recieving inputs from user
# done = False
username = "PiNMAPmqtt"
password = "Christmas"
topic = "NMAP"

#Setting the broker address
broker_address="52.56.169.42"





#Using a unique client id
client = mqtt.Client(randomString(10))

#Assigning the functions to events on the client
client.on_connect=on_connect
client.on_disconnect=on_disconnect
#uncomment to enable logging
# client.on_log=on_log
client.on_message=on_message

print("Connecting to broker ",broker_address)

#connecting to the broker using the certificate, username and password
client.username_pw_set(username, password=password)
client.tls_set(ca_certs="./ca.crt")
client.tls_insecure_set(True)

client.connect(broker_address, 8883, 60)
client.loop_start()

client.subscribe(topic)

#subscribe to the user inputted topic
# while (done == False):
# 	time.sleep(1)

while (1==1):
	time.sleep(1)

client.loop_stop()
client.disconnect()