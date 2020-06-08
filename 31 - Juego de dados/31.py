# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:18:03 2019

@author: Franco
"""

#31 - Juego de dados

import random
import pygame
import time
import sys	#Para cerrar las ventanas / Esta libreria ya viene por defecto

from pygame.locals import *	#Para inicializar todos los modulos que vienen con esa libreria
pygame.init() 

#**************************************************************************************************#

objeto_ventana = pygame.display.set_mode((800,600) )	#Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("Buena suerte")    #Titulo de la pantalla

fondo_de_pantalla = pygame.image.load("Fondo.jpg")
imagen_1 = pygame.image.load("Uno.jpg")
imagen_2 = pygame.image.load("Dos.jpg")
imagen_3 = pygame.image.load("Tres.jpg")
imagen_4 = pygame.image.load("Cuatro.jpg")
imagen_5 = pygame.image.load("Cinco.png")
imagen_6 = pygame.image.load("Seis.png")

miFuente = pygame.font.SysFont("Arial", 40)
color_rojo = (255,0,0)

#**************************************************************************************************#
def cara1_6():
    objeto_ventana.blit(imagen_2,(50,50) )
    objeto_ventana.blit(imagen_3,(600,50) )
    objeto_ventana.blit(imagen_4,(50,375) )
    objeto_ventana.blit(imagen_5,(600,375) )

def cara2_5():
    objeto_ventana.blit(imagen_1,(50,50) )
    objeto_ventana.blit(imagen_3,(600,50) )
    objeto_ventana.blit(imagen_4,(50,375) )
    objeto_ventana.blit(imagen_6,(600,375) )

def cara3_4():
    objeto_ventana.blit(imagen_1,(50,50) )
    objeto_ventana.blit(imagen_2,(600,50) )
    objeto_ventana.blit(imagen_5,(50,375) )
    objeto_ventana.blit(imagen_6,(600,375) )
    
def cambiar_jugador(num_jugador):
    if num_jugador == 1: num_jugador = 2
    else: num_jugador = 1
   
    return num_jugador    
    
    
#**************************************************************************************************#
cara_elegida = random.randint(1,6) #El juego empieza siempre con un numero al azar
total = cara_elegida
num_jugador = 1;
#**************************************************************************************************#  
while True:  #Un while infinito para que no se cierre la ventana
    objeto_ventana.blit(fondo_de_pantalla,(0,0) )
    
    if cara_elegida == 1: objeto_ventana.blit(imagen_1,(325,225) ); cara1_6()
    elif cara_elegida == 6: objeto_ventana.blit(imagen_6,(325,225) ); cara1_6()    
    elif cara_elegida == 2: objeto_ventana.blit(imagen_2,(325,225) ); cara2_5()
    elif cara_elegida == 5: objeto_ventana.blit(imagen_5,(325,225) ); cara2_5()
    elif cara_elegida == 3: objeto_ventana.blit(imagen_3,(325,225) ); cara3_4()
    elif cara_elegida == 4: objeto_ventana.blit(imagen_4,(325,225) ); cara3_4() 
    
    Texto_1 = miFuente.render("Puntaje: " + str(total), 0, color_rojo)
    objeto_ventana.blit(Texto_1, (325,400) )
    Texto_2 = miFuente.render("Turno del Jugador: " + str(num_jugador),0,color_rojo)
    objeto_ventana.blit(Texto_2, (250,25) )
    
    if total >= 31:
        Texto_3 = miFuente.render("PERDISTE",0,color_rojo)
        objeto_ventana.blit(Texto_3, (315, 65) )
        pygame.display.update()
        time.sleep(5)
        cara_elegida = random.randint(1,6) #El juego se reinicia
        total = cara_elegida
        num_jugador = 1;
    
    for evento in pygame.event.get():           #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
        if evento.type == QUIT: pygame.quit(); sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if cara_elegida == 1 or cara_elegida == 6:
                if evento.key == K_2: total += 2; cara_elegida = 2; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_3: total += 3; cara_elegida = 3; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_4: total += 4; cara_elegida = 4; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_5: total += 5; cara_elegida = 5; num_jugador=cambiar_jugador(num_jugador)
                
                
            if cara_elegida == 2 or cara_elegida == 5:
                if evento.key == K_1: total += 1; cara_elegida = 1; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_3: total += 3; cara_elegida = 3; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_4: total += 4; cara_elegida = 4; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_6: total += 6; cara_elegida = 6; num_jugador=cambiar_jugador(num_jugador)
        
            
            if cara_elegida == 3 or cara_elegida == 4:
                if evento.key == K_1: total += 1; cara_elegida = 1; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_2: total += 2; cara_elegida = 2; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_5: total += 5; cara_elegida = 5; num_jugador=cambiar_jugador(num_jugador)
                elif evento.key == K_6: total += 6; cara_elegida = 6; num_jugador=cambiar_jugador(num_jugador)
            
            if evento.key == K_r: total = 0     

    pygame.display.update()                     #Para que se actualize la pantalla    




