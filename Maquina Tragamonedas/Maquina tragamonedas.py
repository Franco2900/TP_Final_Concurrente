# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:45:58 2019

@author: Franco
"""

#Maquina tragamonedas
import random
import pygame
import winsound
import time
pygame.mixer.init()

import sys	#Para cerrar las ventanas / Esta libreria ya viene por defecto
import pygame

from pygame.locals import *	#Para inicializar todos los modulos que vienen con esa libreria
pygame.init() 
#**************************************************************************************************#

#**************************************************************************************************#

objeto_ventana = pygame.display.set_mode((800,600))	#Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("A viciar se ha dicho")		#Titulo de la pantalla

fondo_de_pantalla = pygame.image.load("Fondo.jpg")
imagen_Frutilla = pygame.image.load("Frutilla.jpg")
imagen_Limon = pygame.image.load("Limon.png")
imagen_Estrella = pygame.image.load("Estrella.jpg")
imagen_Campana = pygame.image.load("Campana.jpg")
imagen_MonedaDeOro = pygame.image.load("Moneda de oro.jpg")
imagen_Numero7 = pygame.image.load("7.png")
imagen_Victoria = pygame.image.load("Premio.jpg")
imagen_GranVictoria = pygame.image.load("Gran premio.jpg")
imagen_MalaSuerte = pygame.image.load("Mala suerte.jpg")

dinero = 100
elementos_maquina = ["Frutilla","Limon","Estrella","Campana","Moneda de oro","7"]

#Frutilla = Cantidad de monedas x 2
#Limon = Cantidad de monedas x 3
#Estrella = Cantidad de monedas x 5
#Campana = Cantidad de monedas x 10
#Moneda de oro = Cantidad de monedas x 20
#7 = Cantidad de monedas x 77

#pygame.mixer.music.load("Musica de fondo.mp3")
#pygame.mixer.music.play()

color_negro = (0,0,0)
color_rojo = (255,0,0)
color_azul = (0,0,255)
miFuente = pygame.font.SysFont("Arial", 30)
Texto_1 = miFuente.render("1) 1 moneda" ,0,color_rojo)
Texto_2 = miFuente.render("2) 2 monedas",0,color_azul)
Texto_3 = miFuente.render("3) 3 monedas",0,color_rojo)
Texto_4 = miFuente.render("4) 5 monedas",0,color_azul)
Texto_5 = miFuente.render("5) 10 monedas",0,color_rojo)
Texto_6 = miFuente.render("6) 25 monedas",0,color_azul)
Texto_7 = miFuente.render("7) 50 monedas",0,color_rojo)
Texto_8 = miFuente.render("8) 100 monedas",0,color_azul)
Texto_9 = miFuente.render("0) Salir",0,color_rojo)

opcion = 777

Texto_12 = miFuente.render("No tienes suficiente dinero",0,color_rojo)
Texto_13 = miFuente.render("Apuesta menos o vuelve cuando tengas más dinero",0,color_rojo)

lista_de_opciones=[0, 1, 2, 3, 5, 10, 25, 50, 100]
#clock = pygame.time.Clock()
#************************************************************************************************#

def giro(coordenadaX, coordenadaY):
    variable = random.choice(elementos_maquina)  
    if(variable == "Frutilla"):        objeto_ventana.blit(imagen_Frutilla, (coordenadaX, coordenadaY) )
    elif(variable == "Limon"):         objeto_ventana.blit(imagen_Limon, (coordenadaX, coordenadaY) )
    elif(variable == "Estrella"):      objeto_ventana.blit(imagen_Estrella, (coordenadaX, coordenadaY) )
    elif(variable == "Campana"):       objeto_ventana.blit(imagen_Campana, (coordenadaX, coordenadaY) )
    elif(variable == "Moneda de oro"): objeto_ventana.blit(imagen_MonedaDeOro,(coordenadaX, coordenadaY) )
    elif(variable == "7"):             objeto_ventana.blit(imagen_Numero7,(coordenadaX, coordenadaY) )
    return variable

def azar(dinero):
    i=0
    dinero -= lista_de_opciones[int(opcion)]
    objeto_ventana.blit(fondo_de_pantalla,(0,0) )
    
    while i<48:
        if(i<16):	variable_1=giro(60, 25)
        if(i<32):	variable_2=giro(320, 30)
        if(i<48):	variable_3=giro(575, 35)
        pygame.display.update(); 
        #time.sleep(0.125)	#He aqui el error
		#clock.tick(10)		#time.sleep alterno
        i+=1
    pygame.display.update()
    time.sleep(2)
    
    if variable_1 == variable_2 == variable_3:
        objeto_ventana.blit(imagen_Victoria, (0,0) )
        winsound.PlaySound("Premio.wav",winsound.SND_ASYNC)
        if(variable_1 == "Frutilla"):			dinero += (cantidad_apuesta * 2)
        elif(variable_1 == "Limon"):			dinero += (cantidad_apuesta * 3)
        elif(variable_1 == "Estrella"):		    dinero += (cantidad_apuesta * 5)
        elif(variable_1 == "Campana"):		    dinero += (cantidad_apuesta * 10)
        elif(variable_1 == "Moneda de oro"):	dinero += (cantidad_apuesta * 20)
        elif(variable_1 == "7"):				dinero += (cantidad_apuesta * 77)
    else:	objeto_ventana.blit(imagen_MalaSuerte, (0,0) )
    pygame.display.update()
    time.sleep(5)

    return dinero    

def chequeo():	#Chequeo para saber si tiene suficiente dinero para apostar esa cantidad
	aux_dinero = dinero - lista_de_opciones[int(opcion)]
	if (aux_dinero < 0):
		Texto_11 = miFuente.render("Opcion elegida: " + str(opcion),0,color_rojo)
		objeto_ventana.blit(Texto_11, (0,360) )
		objeto_ventana.blit(Texto_12, (0,400) )
		objeto_ventana.blit(Texto_13, (0,430) )
		pygame.display.update()
		time.sleep(3.5)
		return False #Melchor no te enojes por el return doble
	winsound.PlaySound("Ingreso de ficha.wav",winsound.SND_ASYNC)
	return True

def end():
	pygame.quit()			#Que se cierre la ventana
	sys.exit()

#************************************************************************************************#

while True:
	Texto_10 = miFuente.render("Dinero: " + str(dinero),0,color_azul)
	
	objeto_ventana.fill(color_negro)
	objeto_ventana.blit(Texto_1,(0,0) )
	objeto_ventana.blit(Texto_2,(0,30) )
	objeto_ventana.blit(Texto_3,(0,60) )
	objeto_ventana.blit(Texto_4,(0,90) )
	objeto_ventana.blit(Texto_5,(0,120) )
	objeto_ventana.blit(Texto_6,(0,150) )
	objeto_ventana.blit(Texto_7,(0,180) )
	objeto_ventana.blit(Texto_8,(0,210) )
	objeto_ventana.blit(Texto_9,(0,240) )
	objeto_ventana.blit(Texto_10,(0,300) )

	pygame.display.update()
	for evento in pygame.event.get():		#Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
		if evento.type == QUIT: end()		#En caso de que el usuario aprete la X de la ventana
		elif evento.type == pygame.KEYDOWN:
			if (evento.key == K_1 or evento.key == K_2 or evento.key == K_3 or evento.key == K_4 or evento.key == K_5 or evento.key == K_6 or evento.key == K_7 or evento.key == K_8):
				if evento.key == K_1:	opcion = 1
				elif evento.key == K_2:	opcion = 2
				elif evento.key == K_3:	opcion = 3
				elif evento.key == K_4:	opcion = 4
				elif evento.key == K_5:	opcion = 5
				elif evento.key == K_6:	opcion = 6
				elif evento.key == K_7:	opcion = 7
				elif evento.key == K_8:	opcion = 8
				if chequeo() == True:
					cantidad_apuesta = lista_de_opciones[int(opcion)]
					dinero = azar(dinero)
			elif evento.key == K_0:
				pygame.quit()	 #Que se cierre la ventana
				sys.exit()		#Que se cierre el programa

	pygame.display.update()