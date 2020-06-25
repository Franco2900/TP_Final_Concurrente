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
import os

from pygame.locals import *	#Para inicializar todos los modulos que vienen con esa libreria
pygame.init() 
#**************************************************************************************************#

#**************************************************************************************************#

objeto_ventana = pygame.display.set_mode((800,600))	#Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("A viciar se ha dicho")		#Titulo de la pantalla

fondo_de_pantalla = pygame.image.load("Fondo.jpg")
imagen_Victoria = pygame.image.load("Premio.jpg")
imagen_GranVictoria = pygame.image.load("Gran premio.jpg")
imagen_MalaSuerte = pygame.image.load("Mala suerte.jpg")

dinero = 100
elementos_maquina = ["Frutilla.jpg","Limon.png","Estrella.jpg","Campana.jpg","Moneda de oro.jpg","7.png"]
win_multiplier = [2, 3, 5, 10, 20, 77]

variable_1 = elementos_maquina[0]
variable_2 = elementos_maquina[0]
variable_3 = elementos_maquina[0]

"""pygame.mixer.music.load("Musica de fondo.mp3")
pygame.mixer.music.play()"""

color_negro = (0,0,0)
color_rojo = (255,0,0)
color_azul = (0,0,255)
miFuente = pygame.font.SysFont("Arial", 30)
texto_1 = miFuente.render("1) 1 moneda" ,0,color_rojo)
texto_2 = miFuente.render("2) 2 monedas",0,color_azul)
texto_3 = miFuente.render("3) 3 monedas",0,color_rojo)
texto_4 = miFuente.render("4) 5 monedas",0,color_azul)
texto_5 = miFuente.render("5) 10 monedas",0,color_rojo)
texto_6 = miFuente.render("6) 25 monedas",0,color_azul)
texto_7 = miFuente.render("7) 50 monedas",0,color_rojo)
texto_8 = miFuente.render("8) 100 monedas",0,color_azul)
texto_9 = miFuente.render("0) Salir",0,color_rojo)

opcion = 777

texto_12 = miFuente.render("No tienes suficiente dinero",0,color_rojo)
texto_13 = miFuente.render("Apuesta menos o vuelve cuando tengas más dinero",0,color_rojo)

lista_de_opciones=[0, 1, 2, 3, 5, 10, 25, 50, 100]
#clock = pygame.time.Clock()
#************************************************************************************************#

def giro(coordenadaX, coordenadaY, variable):
	#variable = random.choice(elementos_maquina)
	if elementos_maquina.index(variable)+1 == len(elementos_maquina): variable = elementos_maquina[0]
	else: variable = elementos_maquina[elementos_maquina.index(variable)+1]
	objeto_ventana.blit(pygame.image.load(variable), (coordenadaX, coordenadaY))
	return variable

def azar(dinero):
	variable1 = variable_1
	variable2 = variable_2
	variable3 = variable_3
	objeto_ventana.blit(fondo_de_pantalla,(0,0) )
	objeto_ventana.blit(pygame.image.load(variable1), (60, 25))
	objeto_ventana.blit(pygame.image.load(variable2), (320, 30))
	objeto_ventana.blit(pygame.image.load(variable3), (575, 35))
	pygame.display.update()
	pygame.time.delay(150) #wait(150)
	dinero -= lista_de_opciones[opcion]
	giro1=random.randint(16, 16+len(elementos_maquina)-1)
	giro2=random.randint(32, 32+len(elementos_maquina)-1)
	giro3=random.randint(48, 48+len(elementos_maquina)-1)
	for i in range (54):
		if(i<giro1):	variable1=giro(60, 25, variable1)
		if(i<giro2):	variable2=giro(320, 30, variable2)
		if(i<giro3):	variable3=giro(575, 35, variable3)
		pygame.display.update();
		pygame.time.delay(75) #wait(75)	#time.sleep(0.125)	#He aqui el error.				#clock.tick(10)	#time.sleep alterno
	pygame.display.update()
	pygame.time.delay(500) #wait(500)
	
	if variable1 == variable2 == variable3:
		objeto_ventana.blit(imagen_Victoria, (0,0) )
		winsound.PlaySound("Premio.wav",winsound.SND_ASYNC)
		dinero += cantidad_apuesta * win_multiplier[elementos_maquina.index(variable1)]
	else:	objeto_ventana.blit(imagen_MalaSuerte, (0,0) )
	pygame.display.update()
	pygame.time.delay(2000) #wait(2000)
	return dinero, variable1, variable2, variable3

def chequeo():	#Chequeo para saber si tiene suficiente dinero para apostar esa cantidad, el 2do retorno es por si el usuario presiono la X de la ventana
	aux_dinero = dinero - lista_de_opciones[opcion]
	if (aux_dinero < 0):
		texto_11 = miFuente.render("Opcion elegida: " + str(opcion),0,color_rojo)
		objeto_ventana.blit(texto_11, (0,360) )
		objeto_ventana.blit(texto_12, (0,400) )
		objeto_ventana.blit(texto_13, (0,430) )
		pygame.display.update()
		whileflag=True
		while whileflag: #Demora hasta que el usuario presione una tecla
			for evento in pygame.event.get():
				if evento.type == QUIT:
					return True, False		#En caso de que el usuario aprete la X de la ventana. En este caso la primer variable da lo mismo
				elif evento.type == pygame.KEYDOWN: whileflag=False
		return False, True
	winsound.PlaySound("Ingreso de ficha.wav",winsound.SND_ASYNC)
	return True, True

def wait(tiempo):
	tiempo+=pygame.time.get_ticks()
	while pygame.time.get_ticks() != tiempo: pass

#************************************************************************************************#

playgameflag = True
while playgameflag:
	texto_10 = miFuente.render("Dinero: " + str(dinero),0,color_azul)
	
	objeto_ventana.fill(color_negro)
	objeto_ventana.blit(texto_1,(0,0) )
	objeto_ventana.blit(texto_2,(0,30) )
	objeto_ventana.blit(texto_3,(0,60) )
	objeto_ventana.blit(texto_4,(0,90) )
	objeto_ventana.blit(texto_5,(0,120) )
	objeto_ventana.blit(texto_6,(0,150) )
	objeto_ventana.blit(texto_7,(0,180) )
	objeto_ventana.blit(texto_8,(0,210) )
	objeto_ventana.blit(texto_9,(0,240) )
	objeto_ventana.blit(texto_10,(0,300) )

	pygame.display.update()
	
	loopflag=True
	while loopflag:
		for evento in pygame.event.get():		#Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
			if evento.type == QUIT: #En caso de que el usuario aprete la X de la ventana
				playgameflag = False
				loopflag = False
			elif evento.type == pygame.KEYDOWN:
				if evento.key == K_0:
					playgameflag = False
					loopflag = False
				if (evento.key == K_1 or evento.key == K_2 or evento.key == K_3 or evento.key == K_4 or evento.key == K_5 or evento.key == K_6 or evento.key == K_7 or evento.key == K_8):
					opcion = int(evento.unicode) #Lo mismo que hacer opcion = 1 si evento.key == K_1 etc
					chequeo = chequeo()
					if not chequeo[1]: #Si el jugador presiono la X de la ventana mientras se corria la funcion chequeo()
						playgameflag = False
					elif chequeo[0]: #Si el chequeo comprobo que el dinero seleccionado alcanza para hacer la jugada deseada
						pygame.key.stop_text_input()
						cantidad_apuesta = lista_de_opciones[opcion]
						dinero, variable_1, variable_2, variable_3 = azar(dinero)
						pygame.key.start_text_input()
					loopflag=False
	pygame.display.update()
	pygame.event.clear()

if __name__ != "__main__": 
	os.chdir("..") #Volver el directorio uno para atras, por ejemplo de C:\Archivos de programas a C:\
	import Menu_Principal.py