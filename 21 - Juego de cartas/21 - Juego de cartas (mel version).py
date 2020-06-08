# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:47:11 2019

@author: Franco
"""

########################################################################################################################################
#21
import random
import pygame
import winsound
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

""""""

dinero = 100

"""lista_de_musica = ["Amor eterno.mp3", "Costumbres Rocio Durcal.mp3", "Musica De Guitarra Alegre.mp3"] 
pygame.mixer.music.load(random.choice(lista_de_musica))
pygame.mixer.music.play()"""

types=[" de Basto", " de Copas", " de Oro", " de Espadas"]
mazo = []
for x in range(4):
	for y in range(1, 13):
		mazo.append(str(y)+types[x])

print(mazo)

while True:
	random.shuffle(mazo)
	print ("\nDinero: " + str(dinero))
	opcion = input(" 1) Una moneda \n 2) Dos monedas \n 3) Tres monedas \n 4) Cinco monedas \n 5) Diez monedas \n 6) Veinticinco monedas \n 7) Cincuenta monedas \n 8) Cien monedas \n 0) Salir \n")
	while (opcion.isdigit()==False or int(opcion) < 0 or int(opcion) > 8):
		print ("Opción no valida")
		opcion = input()
	if(int(opcion) == 0): break

	#Chequeo para saber si tiene suficiente dinero para apostar esa cantidad
	lista_de_opciones=[1, 2, 3, 5, 10, 25, 50, 100]
	aux_dinero = -1
	while aux_dinero < 0:
		aux_dinero = dinero - lista_de_opciones[int(opcion)-1]
		if aux_dinero < 0:
			print ("No tienes suficiente dinero. Realiza otro tipo de apuesta o vuelve cuando tengas más dinero")
			opcionaux = opcion
			opcion = input()
			while (not opcion.isdigit() or opcion == opcionaux or int(opcion)<0 or int(opcion)>len(lista_de_opciones)):
				print ("Opción invalida")
				opcion = input()
			if(int(opcion) == 0): break
			aux_dinero = dinero - lista_de_opciones[int(opcion)-1]

	if(int(opcion) == 0): break

	cantidad_apuesta = lista_de_opciones[int(opcion)-1] #En caso de que si se disponga del dinero suficiente se realiza la apuesta
	dinero = dinero - lista_de_opciones[int(opcion)-1]

	jugadoresnumber=2
	manos=[]
	puntajes=[]
	for x in range(jugadoresnumber): #Reparto de cartas
		manos.append([mazo.pop(), mazo.pop()])
		puntajes.append(calcularpuntaje(manos[x]))

	winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)
	print("Tus cartas:", manos[0][0], "-", manos[0][1]) #Mano del jugador 1 carta 1 y mano del jugador 1 carta 2
	print("Tu puntaje:", puntajes[0]) #Puntaje del jugador 1

	#El jugador elige si agarra otra carta o no
	opcion = input("¿Agarrás otra carta? \n 1) Si \n 2) No \n")
	while opcion!="1" and opcion!="2":
		print("Esa no es una opción válida, intentelo de nuevo: ")
		opcion = input()
	if opcion == "1":
		winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)
		manos[0], puntajes[0] = addcard(manos[0])
	if(puntajes[1] <= 11 or (random.randint(1, 10) == 1 and puntajes[1] <=15)): manos[1], puntajes[1] = addcard(manos[1]) #La AI elige si tomar otra carta o no
	
	#Se determina quien gana
	if(puntajes[0] == puntajes[1]):
		print("\nEmpate. Todos recuperan sus apuestas \n")
		dinero += cantidad_apuesta
	elif(puntajes[0] < puntajes[1]): print("\nPerdiste")
	elif(puntajes[0] > puntajes[1]):
		print("\nGanaste")
		dinero += cantidad_apuesta * 2
	if len(manos[0])>2:
		print("Tus cartas:", end=" ")
		for x in range(len(manos[0])-1):
			print(manos[0][x], end= ", ")
		print(manos[0][x+1], "\nTu puntaje:", puntajes[0]) #Imprime la ultima carta del jugador y su puntaje
	print("Cartas del contrincante:", end=" ")
	for x in range(len(manos[1])-1):
		print(manos[1][x], end= ", ")
	print(manos[1][x+1], "\nPuntaje del contricante: ", puntajes[1]) #Imprime la ultima carta del contrincante y su puntaje

	for jugador in manos: #Se devuelven las cartas de todos los jugadores al mazo
		for carta in jugador: mazo.append(carta)

delay = input("Presiona ENTER para terminar")
pygame.mixer.music.stop()