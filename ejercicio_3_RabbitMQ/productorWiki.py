#!/usr/bin/env python
import pika

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de la cola
channel.queue_declare(queue='hello')
search = input("Ingrese su busqueda : ")

#Publicación del mensaje
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(search))

print(" Solicitud realizada. ")

connection.close()