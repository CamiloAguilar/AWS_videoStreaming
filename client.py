import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('18.231.176.132', 443)) #'tcp://18.231.176.132:443

while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        
        # Serialize frame
        data = pickle.dumps(frame)
        
        # Send message length first
        message_size = struct.pack("L", len(data)) ### CHANGED

        # Then data
        client_sock.sendall(message_size + data)
        print('...sending frames to AWS')

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
