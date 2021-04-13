################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

###################################################################################################
#                                       <<<<<MÓDULOS>>>>>
import os
import sys
import socket
import numpy as np
from cryptography.fernet import Fernet
from matplotlib import pyplot as plt

###################################################################################################
#                                       <<<<<MAIN>>>>>
'''PASO 1 - Cargarmos la imagen original'''
img = plt.imread("img.jpg")

'''PASO 2 - Mostrarmos la imagen original'''
plt.title("Imagen Original")
plt.axis("off")
plt.imshow(img)
plt.show()

'''PASO 3 - Generamos la clave'''
clave = Fernet.generate_key()
with open("clave.key","wb") as archivo_clave:
    archivo_clave.write(clave)
clave = open("clave.key","rb").read()

'''PASO 4 - Leemos la imagen original en bytes'''
with open("img.jpg","rb") as archivo_clave:
    imgOB = archivo_clave.read()

'''PASO 5 - Encriptamos la imagen en bytes'''
f = Fernet(clave)
encriptado = f.encrypt(imgOB)

'''PASO 6 - Creamos el archivo encriptado'''
with open("img.tk3","wb") as archivo_clave:
        archivo_clave.write(encriptado)

'''PASO 7 - Establecemos conexión con el cliente / servidor y enviamos el archivo encriptado con la clave'''
cliente = socket.socket()
cliente.connect(("localhost", 6000))
with open("img.tk3","rb") as archivo_clave:
    file = archivo_clave.read()
cliente.send(file)
cliente.shutdown(socket.SHUT_RDWR)
input(">ARCHIVO ENVIADO<")
cliente = socket.socket()
cliente.connect(("localhost", 6000))
with open("clave.key","rb") as archivo_clave:
    file = archivo_clave.read()
cliente.send(file)
cliente.shutdown(socket.SHUT_RDWR)
input(">ARCHIVO ENVIADO<")

'''PASO 12 - Establecemos conexión con el cliente / servidor y recibimos el archivo'''
servidor = socket.socket()
servidor.bind(("localhost", 6001))
servidor.listen(0)
conn, addr = servidor.accept()
with open("imgD.jpg","wb") as archivo_clave:
    data = conn.recv(1024)
    while data:
        archivo_clave.write(data)
        data = conn.recv(1024)
servidor.close()
input(">ARCHIVO RECIBIDO<")

'''PASO 13 - Cargarmos la  imagen recibida'''
img2 = plt.imread("imgD.jpg")

'''PASO 14 - Mostrarmos la imagen recibida'''
plt.title("Imagen Recibida")
plt.axis("off")
plt.imshow(img2)
plt.show()

'''PASO 14 - Comparamos ambas imágenes'''
plt.subplot(1,2,1)
plt.title("Imagen Original")
plt.axis("off")
plt.imshow(img)

plt.subplot(1,2,2)
plt.title("Imagen Recibida")
plt.axis("off")
plt.imshow(img2)
plt.show()

print(np.array_equal(img,img2))