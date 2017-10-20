# server.py 
import socket                                         
import time
import pygame
import pygame.camera
import base64

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8080                                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

#initialize camera
pygame.camera.init()
cams = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cams[0])
cam.start()

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    img = cam.get_image()
    pygame.image.save(img, "current_image.jpg")
    image_data = open('current_image.jpg', 'rb')
    current_data = image_data.read(1024)

    while (current_data):
       clientsocket.send(current_data)
       print('Sent ',repr(current_data))
       current_data = image_data.read(1024)
    #response_data = base64.b64encode(image_data).decode('utf-8')
    
    clientsocket.close()

cam.stop()
