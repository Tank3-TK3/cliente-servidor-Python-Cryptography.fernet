################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

###################################################################################################
#                                       <<<<<MÓDULOS>>>>>
import sys
import socket
import numpy as np
from cryptography.fernet import Fernet
from matplotlib import pyplot as plt

###################################################################################################
#                                       <<<<<MAIN>>>>>
'''PASO 7 - Establecemos conexión con el cliente / servidor y recibimos el archivo encriptado con la clave'''
servidor = socket.socket()
servidor.bind(("localhost", 6000))
servidor.listen(0)
conn, addr = servidor.accept()
with open("img.tk3","wb") as archivo_clave:
    data = conn.recv(1024)
    while data:
        archivo_clave.write(data)
        data = conn.recv(1024)
servidor.close()
input(">ARCHIVO RECIBIDO<")
servidor = socket.socket()
servidor.bind(("localhost", 6000))
servidor.listen(0)
conn, addr = servidor.accept()
with open("clave.key","wb") as archivo_clave:
    data = conn.recv(1024)
    while data:
        archivo_clave.write(data)
        data = conn.recv(1024)
servidor.close()
input(">ARCHIVO RECIBIDO<")

'''PASO 8 - Desencriptamos el archivo recibido'''
clave = open("clave.key","rb").read()
f = Fernet(clave)
desencriptado = f.decrypt(open("img.tk3","rb").read())

'''PASO 9 - Creamos la imagen a partir del archivo desencriptado'''
with open("imgD.jpg","wb") as archivo_clave:
    archivo_clave.write(desencriptado)

'''PASO 10 - Cargarmos la  imagen recibida'''
img = plt.imread("imgD.jpg")

'''PASO 11 - Mostrarmos la imagen recibida'''
plt.title("Imagen Recibida")
plt.axis("off")
plt.imshow(img)
plt.show()

'''PASO 12 - Establecemos conexión con el cliente / servidor y enviamos el archivo devuelta al cliente'''
cliente = socket.socket()
cliente.connect(("localhost", 6001))
with open("imgD.jpg","rb") as archivo_clave:
    file = archivo_clave.read()
cliente.send(file)
cliente.shutdown(socket.SHUT_RDWR)
input(">ARCHIVO ENVIADO<")