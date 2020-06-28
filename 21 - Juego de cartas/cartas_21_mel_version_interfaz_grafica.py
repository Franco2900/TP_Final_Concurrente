# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:47:11 2019

@author: Franco
"""

########################################################################################################################################
#21
import random
import os
import sys 	#Para cerrar las ventanas / Esta libreria ya viene por defecto
import pygame
import winsound
import runpy

pygame.mixer.init()

from pygame.locals import *	#Para inicializar todos los modulos que vienen con esa libreria
pygame.init()

def calcularpuntaje(mano): #Las cartas 11 y 12 valen 10
	cuenta = 0
	for carta in mano:
		if int(carta[0:2])>10: cuenta+= 10
		else: cuenta+= int(carta[0:2])
		if cuenta > 21: cuenta -= 21
	return cuenta

def addcard(mano):
	mano.append(mazo.pop())
	return mano, calcularpuntaje(mano)

def mostrarcarta(carta, coordenada_X, coordenada_Y):
	typestring = carta.split()[2] #Guarda el tipo de carta
	numstring = carta.split()[0]+".jpg"

	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = "cartas-españolas/" + typestring
	abs_file_path = os.path.join(script_dir, rel_path, numstring)

	imagen_carta = pygame.image.load(abs_file_path)
	objeto_ventana.blit(imagen_carta,(coordenada_X, coordenada_Y) )
	pygame.display.update()

def end():
	pygame.quit()			#Que se cierre la ventana
	sys.exit()

def pausa():
	pauseflag = True
	while pauseflag:
		for evento in pygame.event.get():
			if evento.type == QUIT: end()		#En caso de que el usuario aprete la X de la ventana
			elif evento.type == pygame.KEYDOWN: pauseflag = False

def chequeo(opcion, dinero):	#Chequeo para saber si tiene suficiente dinero para apostar esa cantidad
#Chequeo para saber si tiene suficiente dinero para apostar esa cantidad
	aux_dinero = dinero - lista_de_opciones[int(opcion)-1]
	flag = True #Funcion: entrar en while, y servir de retorno a la vez, True = dinero suficiente, False = dinero insuficiente
	if aux_dinero < 0:
		texto_11 = miFuente.render("Opcion elegida: " + str(opcion),0,color_rojo)
		texto_12 = miFuente.render("No tienes suficiente dinero",0,color_rojo)
		texto_13 = miFuente.render("Apuesta menos o vuelve cuando tengas más dinero",0,color_rojo)
		objeto_ventana.blit(texto_11, (0,360) )
		objeto_ventana.blit(texto_12, (0,400) )
		objeto_ventana.blit(texto_13, (0,430) )
		pygame.display.update()
		whileflag = True
		while flag:
			for evento in pygame.event.get():
				if evento.type == QUIT: end()		#En caso de que el usuario aprete la X de la ventana
				elif evento.type == pygame.KEYDOWN: flag = False
	return flag

def imprimir_menu():
	objeto_ventana.fill(color_negro)
	objeto_ventana.blit(texto_0, (0, 0) )
	objeto_ventana.blit(texto_1, (0, 30) )
	objeto_ventana.blit(texto_2, (0, 60) )
	objeto_ventana.blit(texto_3, (0, 90) )
	objeto_ventana.blit(texto_4, (0, 120) )
	objeto_ventana.blit(texto_5, (0, 150) )
	objeto_ventana.blit(texto_6, (0, 180) )
	objeto_ventana.blit(texto_7, (0, 210) )
	objeto_ventana.blit(texto_8, (0, 240) )
	texto = miFuente.render("Dinero: {}".format(dinero), 0, color_rojo) #texto_9 sera usada en otras partes del codigo para imprimir otras cosas
	objeto_ventana.blit(texto, (0, 270) )
	pygame.display.update()

def cardgame(opcion, dinero):
	cantidad_apuesta = lista_de_opciones[int(opcion)-1] #En caso de que si se disponga del dinero suficiente se realiza la apuesta

	jugadoresnumber=2
	manos=[]
	puntajes=[]
	for x in range(jugadoresnumber): #Reparto de cartas
		manos.append([mazo.pop(), mazo.pop()])
		puntajes.append(calcularpuntaje(manos[x]))

	winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)

	mostrarcarta(manos[0][0], 350, 400) #Carta, coordenada X, y coordenada Y
	mostrarcarta(manos[0][1], 400, 400)

	texto = miFuente.render("Tu puntaje: {}".format(puntajes[0]), 0, color_rojo)
	objeto_ventana.blit(texto, (350, 550) )
	pygame.display.update()

	pauseflag = True
	while pauseflag:
		for evento in pygame.event.get():
			if evento.type == QUIT: end()		#En caso de que el usuario aprete la X de la ventana
			elif evento.type == pygame.KEYDOWN:
				if evento.key == K_1:
					winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)
					manos[0], puntajes[0] = addcard(manos[0])
					pauseflag = False
				elif evento.key == K_2: pauseflag = False
	
	if(puntajes[1] <= 11 or (puntajes[1] <=15 and random.randint(1, 10) == 1)): manos[1], puntajes[1] = addcard(manos[1]) #La AI elige si tomar otra carta o no
	
	#Se determina quien gana
	if(puntajes[0] == puntajes[1]): resultado="Empate. Todos recuperan sus apuestas"
	elif(puntajes[0] < puntajes[1]):
		resultado="Perdiste"
		dinero -= cantidad_apuesta
	elif(puntajes[0] > puntajes[1]):
		resultado="Ganaste"
		dinero += cantidad_apuesta
	if len(manos[0])>2:
		imprimir_menu()
		mostrarcarta(manos[0][0], 350, 400)
		mostrarcarta(manos[0][1], 400, 400)
		mostrarcarta(manos[0][2], 450, 400)
		texto = miFuente.render("Tu puntaje: {}".format(puntajes[0]), 0, color_rojo)
		objeto_ventana.blit(texto, (350, 550) )
	coordenada_X = 350
	for x in range(len(manos[1])):
		mostrarcarta(manos[1][x], coordenada_X, 50)
		coordenada_X += 50

	texto = miFuente.render("{}".format(resultado), 0, color_rojo)
	objeto_ventana.blit(texto,(350, 250) )
	texto = miFuente.render("Puntaje del contrincante: {}".format(puntajes[1]), 0, color_rojo)
	objeto_ventana.blit(texto,(300, 0) )
	pygame.display.update()
	pausa()

	for jugador in manos: #Se devuelven las cartas de todos los jugadores al mazo
		for carta in jugador: mazo.append(carta)
	pygame.display.update()
	pygame.time.delay(200)
	return dinero

""""""

objeto_ventana = pygame.display.set_mode((800,600))	#Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("A viciar se ha dicho")		#Titulo de la pantalla

dinero = 100

"""lista_de_musica = ["Amor eterno.mp3", "Costumbres Rocio Durcal.mp3", "Musica De Guitarra Alegre.mp3"] 
pygame.mixer.music.load(random.choice(lista_de_musica))
pygame.mixer.music.play()"""

types=[" de Basto", " de Copa", " de Oro", " de Espada"]
mazo = []
for x in range(4):
	for y in range(1, 13):
		mazo.append(str(y)+types[x])

"""texto_0 = miFuente.render("0) Salir",0,color_rojo)
x = texto_0
for x in range(9):
	miFuente.render("0) 3 monedas",0,color_rojo)
	exec("%s = ")"""

lista_de_opciones=[1, 2, 3, 5, 10, 25, 50, 100]
color_negro = (0, 0, 0)
color_rojo = (255, 0, 0)
color_azul = (0, 0, 255)
miFuente = pygame.font.SysFont("Arial", 30)

texto_0 = miFuente.render("0) Salir", 0, color_rojo)
texto_1 = miFuente.render("1) 1 moneda", 0, color_rojo)
texto_2 = miFuente.render("2) 2 monedas", 0, color_rojo)
texto_3 = miFuente.render("3) 3 monedas", 0, color_rojo)
texto_4 = miFuente.render("4) 5 monedas", 0, color_rojo)
texto_5 = miFuente.render("5) 10 monedas", 0, color_rojo)
texto_6 = miFuente.render("6) 25 monedas", 0, color_rojo)
texto_7 = miFuente.render("7) 50 monedas", 0, color_rojo)
texto_8 = miFuente.render("8) 100 monedas", 0, color_rojo)

playflag = True
while playflag:
	random.shuffle(mazo)
	imprimir_menu()
	for evento in pygame.event.get():
		if evento.type == QUIT: playflag = False	#En caso de que el usuario aprete la X de la ventana
		elif evento.type == pygame.KEYDOWN:
			if evento.key == K_0: playflag = False
			elif (evento.key == K_1 or evento.key == K_2 or evento.key == K_3 or evento.key == K_4 or evento.key == K_5 or evento.key == K_6 or evento.key == K_7 or evento.key == K_8):
				opcion = int(evento.unicode) #Lo mismo que hacer opcion = 1 si evento.key == K_1 etc
				if chequeo(opcion, dinero):
					winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)
					dinero = cardgame(opcion, dinero)

pygame.mixer.music.stop()

if __name__ != "__main__":
    os.chdir("..") #Volver el directorio uno para atras, por ejemplo de C:\Archivos de programas a C:\
    runpy.run_path("Menu_Principal.py")