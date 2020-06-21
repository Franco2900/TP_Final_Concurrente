# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:46:39 2020

@author: Franco
"""
#Librerias y modulos
import sys
import pygame
import threading    #Sirve para crear hilos
import time

from pygame.locals import *
pygame.init()

#############################################################################################################
#Clases y funciones
class MyThread(threading.Thread): #Dentro del parentesis creo un hilo
    
    def __init__(self, name, retraso):  #Inicializo el hilo
        threading.Thread.__init__(self) #Llamo a la clase padre #AVERIGUAR BIEN QUE HACE
        self.name = name
        self.retraso = retraso

    def run(self):  #Ejecuta el hilo
        Texto_2 = miFuente.render('Empezando hilo %s.' % self.name, 0, color_rojo)
        objeto_ventana.blit(Texto_2, (0, 40) )
        hilo_cuenta_atras(self.name, self.retraso)
        print('Terminando hilo %s.' % self.name)

def hilo_cuenta_atras(name, retraso):
    contador = 5

    while contador:
        time.sleep(retraso)
        print('Hilo %s cuenta atras: %i...' % (name, contador))
        contador -= 1
        
############################################################################################################
#Atributos
objeto_ventana = pygame.display.set_mode((800,600))   
pygame.display.set_caption("Hola soy una ventana")
        
color_negro = (0, 0, 0)
color_rojo = (255, 0, 0)
color_verde = (0, 255, 0)
color_azul = (0, 0, 255)

miFuente = pygame.font.SysFont("Arial", 25) 

minutos = 0
segundos = 0

thread1 = MyThread('A', 0.5) #Primer comando que encuentra
thread2 = MyThread('B', 0.5)

thread1.start() #Inicio nuevo hilo
thread2.start()
#############################################################################################################
#Codigo Principal
while True:                                     #Un while infinito para que no se cierre la ventana
    
    objeto_ventana.fill(color_negro)
    Texto_1 = miFuente.render("Tiempo transcurrido: " + str(minutos) + ":" + str(segundos), 0, color_rojo)
    objeto_ventana.blit(Texto_1, (0,0) )
    

    thread1.join() #Une los nuevos hilos a un tercero para que funcionen juntos
    thread2.join()
    
    segundos +=1
    if segundos == 60:
        minutos += 1
        segundos = 0
        
    pygame.display.update()
    time.sleep(1)
    
    for evento in pygame.event.get():           #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
        if evento.type == QUIT:                 #En caso de que el usuario aprete la X de la ventana
            pygame.quit()                       #Que se cierre la ventana
            sys.exit()
    
    pygame.display.update()                     #Para que se actualize la pantalla
