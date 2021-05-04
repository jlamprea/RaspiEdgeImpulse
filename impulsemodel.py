import cv2
import time
import numpy as np
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # se llaman la salida por el GPIO
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

def now():
    return round(time.time() * 1000) # para tomar una medida del frame

from edge_impulse_linux.image import ImageImpulseRunner #CLI de edge impulse
#el modelo se debe descargar con el comando edege-impulse-linux-runner -download modelfile.eim
model= os.path.join("/home/pi","modelfile.eim") # path onde esta el modelo
print("Model: ",model)
with ImageImpulseRunner(model) as runner:  #instancia al modelo
        model_info= runner.init() # se inicia el modelo
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
        labels = model_info['model_parameters']['labels'] # se imprime labels
        print(labels)
        next_frame = 0 # limit to ~10 fps here
        
        for res, img in runner.classifier(0): # se corre el modelo, deprende la camara
            if (next_frame > now()):
                time.sleep((next_frame - now()) / 1000)
        
            print('classification runner response', res["result"]["classification"])
            if res["result"]["classification"]["PataconQuemao"]>=0.6:
                GPIO.output(2,GPIO.HIGH) # se prende LED GPIO2
            else:
                GPIO.output(2,GPIO.LOW)

            next_frame = now() + 100
            cv2.imshow('edgeimpulse', img) # muestra la imagen
            if cv2.waitKey(20)& 0xFF== ord("s"):
                break
     
    