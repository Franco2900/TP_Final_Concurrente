# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:43:52 2019

@author: Franco
"""
            
#Ruleta casino
import random
import pygame
import winsound
pygame.mixer.init()

dinero = 100

#pygame.mixer.music.load("Musica de fondo.mp3")
#pygame.mixer.music.play()

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
    
    #Tipo de apuesta realizada
    print ("Selecciona tu tipo de apuesta \n")
    print (" 1)  Simple           (Ganancia = Apuesta x 35)")
    print (" 2)  Doble            (Ganancia = Apuesta x 17)")
    print (" 3)  Cuadruple        (Ganancia = Apuesta x 8)")
    print (" 4)  Una docena       (Ganancia = Apuesta x 3)")
    print (" 5)  Una fila         (Ganancia = Apuesta x 3)")
    #1° docena = Del 1 al 12
    #2° docena = Del 13 al 24
    #3° docena = Del 25 al 36
    print (" 6)  Del 1 al 18      (Ganancia = Apuesta x 2)")
    print (" 7)  Del 19 al 36     (Ganancia = Apuesta x 2)")
    print (" 8)  Impares          (Ganancia = Apuesta x 2)")
    print (" 9)  Pares            (Ganancia = Apuesta x 2)")
    print (" 10) Todas las rojas  (Ganancia = Apuesta x 2)")
    print (" 11) Todas las negras (Ganancia = Apuesta x 2)")
    print (" 12) Dos docenas      (Ganancia = Apuesta x 1.5)")
    #1° y 2° docena  (Ganancia = Apuesta x 1.5)
    #1° y 3° docena  (Ganancia = Apuesta x 1.5)
    #2° y 3° docena  (Ganancia = Apuesta x 1.5)
    
    tipo_apuesta = input()
 ##################################################################################################################
 #Apuesta Simple
    if(int(tipo_apuesta) == 1):
        while True:
            numero_elegido = input("Selecciona un numero entre 0 y 36 \n")
            
            #Se chequea que se haya elegido una opción valida
            bandera = False
            i = 0
            
            while numero_elegido.isdigit() == False:
                numero_elegido = input("Intentelo de nuevo: ")
            
            while (i <= 36):
                if(int(numero_elegido) == i):
                    bandera = True
                i = i + 1
            
            if(bandera == False):
                print ("Esa no es una opción valida")
        
            elif(bandera == True):
                break
        
        
        numero_ruleta = random.randint(0, 36)
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        if(numero_elegido == numero_ruleta):
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 35)
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
    
#####################################################################################################################
#Apuesta Doble  
    if(int(tipo_apuesta) == 2):
        pygame.mixer.music.load("Ruleta casino.mp3")
        pygame.mixer.music.play()
        dinero = dinero + (cantidad_apuesta * 17)

#####################################################################################################################
#Apuesta Cuadruple   
    if(int(tipo_apuesta) == 3):
        pygame.mixer.music.load("Ruleta casino.mp3")
        pygame.mixer.music.play()
        dinero = dinero + (cantidad_apuesta * 8)

#####################################################################################################################
#Apuesta Docena
    if(int(tipo_apuesta) == 4):
        
        docena_1 = [1,2,3,4,5,6,7,8,9,10,11,12]
        docena_2 = [13,14,15,16,17,18,19,20,21,22,23,24]
        docena_3 = [25,26,27,28,29,30,31,32,33,34,35,36]
        
        opcion_2 = input("Eliga una docena \n 1) 1° Docena \n 2) 2° Docena \n 3) 3° Docena \n")
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        
        if(int(opcion_2) == 1):
            while (i <= 11):
                if(numero_ruleta == docena_1[i]):
                    bandera = True
                i = i + 1
        
        if(int(opcion_2) == 2):
            while (i <= 11):
                if(numero_ruleta == docena_2[i]):
                    bandera = True
                i = i + 1
        
        if(int(opcion_2) == 3):
            while (i <= 11):
                if(numero_ruleta == docena_3[i]):
                    bandera = True
                i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 3)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))

#####################################################################################################################       
#Apuesta Fila
    if(int(tipo_apuesta) == 5):
        
        fila_1 = [1,4,7,10,13,16,19,22,25,28,31,34]
        fila_2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        fila_3 = [3,6,9,12,15,18,21,24,27,30,33,36]
        
        opcion_2 = input("Eliga una fila \n 1) 1° Fila \n 2) 2° Fila \n 3) 3° Fila \n")
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        
        if(int(opcion_2) == 1):
            while (i <= 11):
                if(numero_ruleta == fila_1[i]):
                    bandera = True
                i = i + 1
        
        if(int(opcion_2) == 2):
            while (i <= 11):
                if(numero_ruleta == fila_2[i]):
                    bandera = True
                i = i + 1
        
        if(int(opcion_2) == 3):
            while (i <= 11):
                if(numero_ruleta == fila_3[i]):
                    bandera = True
                i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 3)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
        
#####################################################################################################################
#Apuesta del 1 al 18
    if(int(tipo_apuesta) == 6):
        
        numeros_menores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        
        numero_ruleta = random.randint(0, 36)
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_menores[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
        
#####################################################################################################################
#Apuesta del 19 al 36
    if(int(tipo_apuesta) == 7):
        
        numeros_mayores = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        
        numero_ruleta = random.randint(0, 36)
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_mayores[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))        
        
#####################################################################################################################
#Apuesta Impares
    if(int(tipo_apuesta) == 8):
        
        numeros_impares = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
        numero_ruleta = random.randint(0, 36)
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_impares[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
        
#####################################################################################################################
#Apuesta Pares 
    if(int(tipo_apuesta) == 9):
        
        numeros_pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
        numero_ruleta = random.randint(0, 36)
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_pares[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))

#####################################################################################################################
#Apuesta Todas las rojas 
    if(int(tipo_apuesta) == 10):
        
        numeros_rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        numero_ruleta = random.randint(0, 36)
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_rojos[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
            
#####################################################################################################################      
#Apuesta Todas las negras
    if(int(tipo_apuesta) == 11):
        
        numeros_negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        numero_ruleta = random.randint(0, 36)
        
        winsound.PlaySound("Ruleta Casino.wav",winsound.SND_ASYNC)
        
        bandera = False
        i=0
        while (i <= 17):
            if(numero_ruleta == numeros_negros[i]):
                bandera = True
            i = i + 1
            
        if(bandera == True):  
            print ("Felicitaciones")
            dinero = dinero + (cantidad_apuesta * 2)
            print ("El numero que salio es: " + str(numero_ruleta))
        else:
            print ("Perdiste. El numero que salio es: " + str(numero_ruleta))
 
#####################################################################################################################       
#Apuesta Dos docenas
    if(int(tipo_apuesta) == 12):
        pygame.mixer.music.load("Ruleta casino.mp3")
        pygame.mixer.music.play()
        dinero = dinero + (cantidad_apuesta * 1.5)
        
        
        
        
delay = input("Presiona ENTER para terminar")
pygame.mixer.music.stop()
