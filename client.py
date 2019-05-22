#import base64
import cv2
#import zmq
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient # Import the AWS IoT Device SDK
import json # Import json for parson endpoint.json file

# Load the endpoint from file
with open('./AWS_IoT/endpoint.json') as json_file:  
    data = json.load(json_file)

# temporalmente nos conectamo al dispositivo 'car1'
deviceName = 'car1'

# Build useful variable for code
#subTopic = 'edx/messaging/' + deviceName
pubTopic = 'edx/messaging/' + deviceName #destinationDeviceName
keyPath = './AWS_IoT/private.pem.key'
certPath = './AWS_IoT/certificate.pem.crt'
caPath = './AWS_IoT/root-CA.crt'
clientId = deviceName
host = data['endpointAddress']
port = 8883

#********************************************************
## Nos conectamos a AWS IoT usando las credenciales
#********************************************************
# Create an AWS IoT MQTT Client using TLSv1.2 Mutual Authentication
myAWSIoTMQTTClient = AWSIoTMQTTClient(deviceName)

# configureEndpoint
myAWSIoTMQTTClient.configureEndpoint(host, port)

# configureCredentials
myAWSIoTMQTTClient.configureCredentials(caPath, keyPath, certPath)

# Conectese al servicio AWS IoT mediante la funcion de conexion
myAWSIoTMQTTClient.connect()

# Function to publish payload to IoT topic
def publishToIoTTopic(topic, payload):
    # TODO 4: Implement function to publish to specified IoT topic using device object
    #         that you will create
    myAWSIoTMQTTClient.publish(topic, payload, 1)




camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)

        # Calling function to publish to IoT Topic
        print('...enviando informacion a AWS')
        publishToIoTTopic(pubTopic, 'gonocuca')

        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
        	break

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break