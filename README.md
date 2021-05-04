# RaspiEdgeImpulse
Detector de paracones quemados usando Raspberry 3B+ python y edge Impulse como platadorma TinyML

Machine Learning pipeline.

Crear cuenta gratis en edge impulse.
Crear nuevo proyecto y seleccionar imagen classification
Se creará un proyecto par compurer Vision Imagen Classification.
Crear un dataset de training:
Escribir el nombre dela etiqueta LaBEL y tomar minimo 50 fotografias con la raspberry de 640 x 480 de tamaño. Se puede usar OpenCV o directamente de la Picamera.
No usar el Smartphone para toma de fotografias, es distinto la calidad de la foto a la PiCamera, lo mejor es hacer el dataset con la misma camara con la que se va a inferir.
Hacer 50 fotografias por cada Label, PataconBueno, PataconQuemado, Desconocido. con Data acquisition.
Dividir el trainset en trainig y test. 5 fotos por cada label para el testset. Asi se prueba el modelo su presición.
Crear el modelo DNN con Impulse Desing con transfer learning.
Generar features y entrenar el modelo con minimo 50 Epoc o number of training cycle, learning rate 0,0005, Data Augmentation activado y Minimum confidence rating 0.60.
el modelo debe tener un rendimiento de accuracy 0.99 y loss 0.14. de lo contrario modificar valoresanteriores.
En model Testing, clasificar todo y probar el modelo con todo el testset.  la accuracy 84.4%, la matriz de confusión lo ideal es tener valores de 1 en la diagonal y cero en los demas. F1 debe estar cerca a 1.
Deployment. Generar el modelo para cargarlo en la Raspberry. Hacerlo en Linux board ya que estamos con el sistemaa operativo raspbian para la Raspi.
Descarga un archivo modelfile.eim el cual se utiliza para programar mas adelante con python.
Seguir las instrucciones para instalar el CLI Linux en la raspberry en la seccion de documentacion. Mejor si ya tiene lista la Raspi con contror SSH con Vnc.
Seguir a partir del punto 2. 
Conectar la Raspi con el comando edge-impulse-linux y verificar que esta conectado en al dashboard del edge Impulse.
Puede ya correr su modelo en la raspberry directamente con el comando edge-impulse-linux-runner, le pedira login an pass de edge impulse y elegir el proyecto. Con eso puede probar el modelo con la camara de la Raspi.
Para programar con Phython y poder controlar los GPIO. siga las instrucciones para descargar el SDK de linux para python. en Linux SDK, python SDK. 
De los ejemplos que tiene Edge impulse. elija Camera para hacer su archivo plantilla en python. El archivo en este Repo impulsemodel.py esta explicado como usar el modelo y la libreria de GPIO para activar las salidas de acuerdo a la inferencia del modelo.




