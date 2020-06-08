# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:47:11 2019

@author: Franco
"""

def mostrarResultados(carta_1_jugador, carta_2_jugador, carta_3_jugador, carta_1_cpu, carta_2_cpu, carta_3_cpu, puntaje_jugador, puntaje_cpu):
    #Si no agarro una tercer carta que muestre esto
    if(carta_3_jugador == 0):
        print("Tus cartas: " + str(carta_1_jugador) + "-" + str(carta_2_jugador) )
    else:
        print("Tus cartas: " + str(carta_1_jugador) + "-" + str(carta_2_jugador) + "-" + str(carta_3_jugador) )
    print("Tu puntaje: " + str(puntaje_jugador) + "\n")
        
    #Si no agarro una tercer carta que muestre esto
    if(carta_3_cpu == 0):
        print("Cartas del contrincante: " + str(carta_1_cpu) + "-" + str(carta_2_cpu) )
    else:
        print("Cartas del contrincante: " + str(carta_1_cpu) + "-" + str(carta_2_cpu) + "-" + str(carta_3_cpu) )
    print("Puntaje del contricante: " + str(puntaje_cpu) + "\n")    
########################################################################################################################################
#21
import random
import pygame
import winsound
pygame.mixer.init()

dinero = 100

lista_de_musica = ["Amor eterno.mp3", "Costumbres Rocio Durcal.mp3", "Musica De Guitarra Alegre.mp3"] 

pygame.mixer.music.load(random.choice(lista_de_musica))
pygame.mixer.music.play()


while True:
    
    print ("Dinero: " + str(dinero))
    opcion = input(" 1) Una moneda \n 2) Dos monedas \n 3) Tres monedas \n 4) Cinco monedas \n 5) Diez monedas \n 6) Veinticinco monedas \n 7) Cincuenta monedas \n 8) Cien monedas \n 0) Salir \n")
    while (int(opcion) != 1  and int(opcion) != 2 and int(opcion) != 3 and int(opcion) != 4 and int(opcion) != 5 and int(opcion) != 6 and int(opcion) != 7 and int(opcion) != 8 and int(opcion) != 0):
        print ("Opción no valida")
        opcion = input()
    
    
    if(int(opcion) == 0):
        break
    
    #Chequeo para saber si tiene suficiente dinero para apostar esa cantidad    
    while True:
        lista_de_opciones=[0, 1, 2, 3, 5, 10, 25, 50, 100]
        aux_dinero = dinero - lista_de_opciones[int(opcion)]
        
        while (aux_dinero < 0):
            print ("No tienes suficiente dinero. Realiza otro tipo de apuesta o vuelve cuando tengas más dinero")
            aux_dinero = dinero
            opcionaux = opcion
            opcion = input()
            
            while (opcion == opcionaux):
                print ("Ya te dijimos que selecciones otra opción")
                opcionaux = opcion
                opcion = input()
            
            aux_dinero = dinero - lista_de_opciones[int(opcion)]
          
        break
    
    if(int(opcion) == 0):
        break    
        
    #En caso de que si se disponga del dinero suficiente se realiza la apuesta
    cantidad_apuesta = lista_de_opciones[int(opcion)]
    dinero = dinero - lista_de_opciones[int(opcion)]
    
    #Reparto de cartas (El 10, el 11 y el 12 valen lo mismo, las tres cartas valen 10)
    carta_1_jugador = random.randint(1,10)
    carta_2_jugador = random.randint(1,10)
    carta_3_jugador = 0
    
    carta_1_cpu = random.randint(1,10)
    carta_2_cpu = random.randint(1,10)
    carta_3_cpu = 0
    
    puntaje_jugador = carta_1_jugador + carta_2_jugador
    puntaje_cpu = carta_1_cpu + carta_2_cpu
    
    print("Tus cartas: " + str(carta_1_jugador) + "-" + str(carta_2_jugador))
    print("Tu puntaje: " + str(puntaje_jugador) )
    
    #El jugador elige si agarra otra carta o no
    while True:
        opcion = input("¿Agarras otra carta? \n 1) Si \n 2) No \n")
        if(int(opcion) == 1):
            winsound.PlaySound("Entregar una carta.wav",winsound.SND_ASYNC)
            carta_3_jugador = random.randint(1,10)
            puntaje_jugador = puntaje_jugador + carta_3_jugador
            break
        if(int(opcion) == 2):
            break
        print("Esa no es una opción valida")
    
    
    #La maquina elige si agarra otra carta o no
    if(puntaje_cpu <= 11):
        carta_3_cpu = random.randint(1,10)
        puntaje_cpu = puntaje_cpu + carta_3_cpu
    else:   #La maquina decide si arriesgarse a pasarse de 21 o no
        opcion_cpu = random.randint(0,1)
        if(opcion_cpu == 1):
            carta_3_cpu = random.randint(1,10)
            puntaje_cpu = puntaje_cpu + carta_3_cpu
    
    #En caso de que las cartas se pasen de 21
    if(puntaje_jugador > 21): puntaje_jugador -= 21
    if(puntaje_cpu > 21): puntaje_cpu -= 21
    
    
    #Se determina quien gana
    if(puntaje_jugador == puntaje_cpu):
        print("\nEmpate. Todos recuperan sus apuestas \n")
        mostrarResultados(carta_1_jugador, carta_2_jugador, carta_3_jugador, carta_1_cpu, carta_2_cpu, carta_3_cpu, puntaje_jugador, puntaje_cpu)
        dinero += cantidad_apuesta
        
    elif(puntaje_jugador < puntaje_cpu):
        print("\nPerdiste")
        mostrarResultados(carta_1_jugador, carta_2_jugador, carta_3_jugador, carta_1_cpu, carta_2_cpu, carta_3_cpu, puntaje_jugador, puntaje_cpu)
        
    elif(puntaje_jugador > puntaje_cpu):
        print("\nGanaste")
        mostrarResultados(carta_1_jugador, carta_2_jugador, carta_3_jugador, carta_1_cpu, carta_2_cpu, carta_3_cpu, puntaje_jugador, puntaje_cpu)
        dinero = dinero + (cantidad_apuesta * 2)
    
    
delay = input("Presiona ENTER para terminar")
pygame.mixer.music.stop()