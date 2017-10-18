from django.http import HttpResponse
import pygame
import pygame.camera
from django.http import JsonResponse
import base64
import json

# Create your views here.

def index(request):
    pygame.camera.init()
    cams = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cams[0])
    cam.start()
    img = cam.get_image()
    cam.stop()
    pygame.image.save(img, "current_image.jpg")
    image_data = open('current_image.jpg', 'rb').read()
    
    response_data = {}
    response_data['encoded_image_data'] = base64.b64encode(image_data).decode('utf-8')
    print(type(response_data['encoded_image_data']))
    return JsonResponse(response_data)
    #return HttpResponse(image_data, content_type='image/png')
    