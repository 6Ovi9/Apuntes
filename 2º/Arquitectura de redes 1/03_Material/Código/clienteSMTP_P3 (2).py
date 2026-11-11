# -*- coding: utf-8 -*-
from socket import *

#El servidor del correo al que nos vamos a conectar
SERVER_IP = 'XX.XX.XX.XX'   # Introducir la dirección del servidor que proporcione el profesor.
SERVER_PORT = XXXX          # Introducir el puerto del servidor que proporcione el profesor.

#El cuerpo del mensaje puede ser más largo, lo escribimos primero
#Si queremos añadir saltos de línea usamos \r\n
MENSAJE = 'Hola,\r\nEste es un correo de prueba\r\n'
#Para finalizar en envío de texto, se debe enviar "."
MENSAJE = MENSAJE + '\r\n.\r\n'

#Lista de tuplas (orden, código de respuesta) que se van a enviar
LISTA_ORDDENES = [('HELO PuestoXX\r\n', 250),
                  ('XXXXXXXXX', XXX),
                  ('XXXXXXXXX', XXX),
                  ('XXXXXXXXX', XXX),
                  (MENSAJE, 250),
                  ('XXXXXXXXX', XXX)]

#Establecemos conexión con el servidor
clientSocket = XXXXXX(AF_INET, SOCK_STREAM)
clientSocket.XXXXXX((SERVER_IP, SERVER_PORT))

#Recibimos respuesta
recv1 = clientSocket.XXXXXX(1024).decode('utf-8')
print(recv1)

#Por cada entrada de la lista, enviamos la orden, esperamos respuesta
#y procesamos la respuesta
for orden_actual in LISTA_ORDDENES:
    #PASO 1: enviar orden
    clientSocket.XXXXXX(orden_actual[0].encode('utf-8'))

    #PASO 2: recibimos respuesta y la imprimimos en pantalla
    recv1 = clientSocket.XXXXXX(1024).decode('utf-8')
    print(recv1)

    #PASO 3: procesamos la respuesta
    #comprobamos si el código de respuesta recibido se corresponde con el esperado
    if orden_actual[1] != int(recv1[:3]):
        #Si el código es diferente, se ha producido un error.
        #finalizamos bucle porque el proceso del envío del correo no se podrá completar
        print('Error: se ha recibido el código', recv1[:3], 'y se esperaba el', orden_actual[1])
        break
