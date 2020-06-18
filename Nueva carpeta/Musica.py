# -*- coding: utf-8 -*-

import sys
import pygame

from pygame.locals import *    #Para inicializar todos los modulos que vienen con esa libreria
pygame.init()

objeto_ventana = pygame.display.set_mode((1300,600))    #Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("Hola soy una ventana")     #Titulo de la pantalla


color_negro = (0,0,0)
color_rojo = (255,0,0)

miFuente = pygame.font.SysFont("Arial", 30)
Texto_1 = miFuente.render("1) Casino Night" ,0,color_rojo)
Texto_2 = miFuente.render("2) Studiopolis",0,color_rojo)
Texto_3 = miFuente.render("3) Mirage Saloon",0,color_rojo)
Texto_4 = miFuente.render("4) Stardust Speedway",0,color_rojo)
Texto_5 = miFuente.render("5) Chemical",0,color_rojo)
Texto_6 = miFuente.render("6) Emerald Hill",0,color_rojo)

Texto_7 = miFuente.render("Reproduciendo: Jazz - Rap",0,color_rojo)

pygame.mixer.music.load("Jazz - Rap.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1.0)   
            
while True:                                     #Un while infinito para que no se cierre la ventana
    
    sonido = pygame.mixer.music.get_volume()
    Texto_8 = miFuente.render("Sonido: " + str(sonido),0,color_rojo)
    
    objeto_ventana.fill(color_negro)
    objeto_ventana.blit(Texto_1, (0,0) )
    objeto_ventana.blit(Texto_2, (0,35) )
    objeto_ventana.blit(Texto_3, (0,65) )
    objeto_ventana.blit(Texto_4, (0,95) )
    objeto_ventana.blit(Texto_5, (0,125) )
    objeto_ventana.blit(Texto_6, (0,155) )
    objeto_ventana.blit(Texto_7, (0,215) ) 
    objeto_ventana.blit(Texto_8, (0,245) )
    
    for evento in pygame.event.get():           #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
       if evento.type == QUIT:
           pygame.quit()                       #Que se cierre la ventana
           sys.exit()
       elif evento.type == pygame.KEYDOWN:
           if evento.key == K_1:
               pygame.mixer.music.load("Casino Night.mp3")
               pygame.mixer.music.play()
               Texto_7 = miFuente.render("Reproduciendo: Casino Night",0,color_rojo)
           elif evento.key == K_2:
               pygame.mixer.music.load("Studiopolis.mp3")
               pygame.mixer.music.play()
               Texto_7 = miFuente.render("Reproduciendo: Studiopolis",0,color_rojo)
           elif evento.key == K_3:
               pygame.mixer.music.load("Mirage Saloon.mp3")
               pygame.mixer.music.play()
               Texto_7 = miFuente.render("Reproduciendo: Mirage Saloon",0,color_rojo)
           elif evento.key == K_4:
               pygame.mixer.music.load("Stardust Speedway.mp3")
               pygame.mixer.music.play()
               Texto_7 = miFuente.render("Reproduciendo: Stardust Speedway",0,color_rojo)
           elif evento.key == K_5:
               pygame.mixer.music.load("Chemical.mp3")
               pygame.mixer.music.play()
               Texto_7 = miFuente.render("Reproduciendo: Chemical",0,color_rojo)
           elif evento.key == K_6:
               pygame.mixer.music.load("Emerald Hill.mp3")
               pygame.mixer.music.play()    
               Texto_7 = miFuente.render("Reproduciendo: Emerald Hill",0,color_rojo)
           elif evento.key == K_DOWN:
               sonido = sonido - 0.01
               pygame.mixer.music.set_volume(sonido)
           elif evento.key == K_UP:
               sonido = sonido + 0.01
               pygame.mixer.music.set_volume(sonido)
        
    pygame.display.update()                     #Para que se actualize la pantalla
    
    
    
pygame.mixer.music.stop()