# -*- coding: utf-8 -*-
#Ruleta Rusa
import random
import pygame
import winsound
import time
import sys    #Para cerrar las ventanas / Esta libreria ya viene por defecto
from moviepy.editor import *

from pygame.locals import *    #Para inicializar todos los modulos que vienen con esa libreria
pygame.init() 

#*************************************************************************************************#

objeto_ventana = pygame.display.set_mode((800,600))    #Tamaño de la ventana (Ancho/Alto) Si esta vacio, tiene el mismo tamaño que el monitor
pygame.display.set_caption("Buena suerte")    #Titulo de la pantalla

clip = VideoFileClip('Video de intro.mp4')
clip.preview()

pygame.init()
#pygame.mixer.music.load("Musica de fondo dramatica.mp3")
#pygame.mixer.music.play()

#*************************************************************************************************#
dinero = 10000
suerte = ["Vida","Vida","Vida","Muerte","Vida","Vida"]


color_negro = (0, 0, 0)
color_rojo = (255, 0, 0)
color_verde = (0, 255, 0)
color_azul = (0, 0, 255)

miFuente = pygame.font.SysFont("Arial", 25) #Con None se crea una fuente predeterminada
miFuente_2 = pygame.font.SysFont("Cambria", 50)
miFuente_3 = pygame.font.SysFont("Cambria", 30)

Texto_1 = miFuente.render("Presiona Z para apretar el gatillo", 0, color_azul) #Al texto le ponemos la fuente que creamos
Texto_2 = miFuente.render("Presiona X para abandonar (pierdes todo tu dinero pero mejor que perder la vida)", 0, color_azul )


Texto_3 = miFuente_2.render("TU TURNO",0,color_rojo)
Texto_4 = miFuente_2.render("SOBREVIVISTE, por ahora",0,color_verde)

Texto_5 = miFuente_2.render("TURNO DEL CONTRINCANTE",0,color_azul)
Texto_6 = miFuente_2.render("Solo tuviste suerte",0,color_verde)
Texto_7 = miFuente_2.render("A que no te animas a jugar de nuevo",0,color_verde)
Texto_8 = miFuente_2.render("Sigue vivo",0,color_rojo)
Texto_9 = miFuente_3.render("Te toca enfrentar al destino de vuelta",0,color_rojo)

imagen_Muerte = pygame.image.load("Has muerto.jpg")
imagen_Quiebra = pygame.image.load("Quiebra.jpg")
#*************************************************************************************************#

def mostrar_mensaje(mensaje, coordenadas):
    objeto_ventana.fill(color_negro)
    objeto_ventana.blit(mensaje, coordenadas)
    pygame.display.update()
    time.sleep(2)

def disparar():
    clip.preview(fps=60, audio=False)
    pygame.mixer.music.load("Disparo.mp3")
    pygame.mixer.music.play()
    time.sleep(2)

#*************************************************************************************************#
while True:
    
    objeto_ventana.fill(color_negro)
    objeto_ventana.blit(Texto_1, (0,0) )
    objeto_ventana.blit(Texto_2, (0,40) )
    
    Texto_0 = miFuente.render("Dinero: " + str(dinero), 0, color_azul)
    objeto_ventana.blit(Texto_0, (0,120) )
    
    pygame.display.update()   #Para que se actualize la pantalla
    
    
    for evento in pygame.event.get():           #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
        if evento.type == QUIT:                 #En caso de que el usuario aprete la X de la ventana
            pygame.quit()                       #Que se cierre la ventana
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
          if evento.key == K_z:
              destino = random.choice(suerte)
              mostrar_mensaje(Texto_3, (300,225) )
              if (destino == "Muerte"):
                clip = VideoFileClip('Jugador muere.mp4')
                disparar()
                clip.close()
                objeto_ventana.blit(imagen_Muerte, (0,0) )
                winsound.PlaySound("Muerte.wav",winsound.SND_ASYNC)
                pygame.display.update()
                time.sleep(5)
              else:
                clip = VideoFileClip('Jugador sigue vivo.mp4')
                clip.preview(fps=60, audio=False)
                clip.close()
                mostrar_mensaje(Texto_4, (100,200) )
                destino = random.choice(suerte)
                mostrar_mensaje(Texto_5, (100,225) )
                if (destino == "Muerte"):
                  clip = VideoFileClip('CPU muere.mp4')  
                  disparar()
                  clip.close()
                  mostrar_mensaje(Texto_6, (0,225) )
                  mostrar_mensaje(Texto_7, (0,280) )
                  time.sleep(5)
                  dinero = dinero + 10000
                else:
                  clip = VideoFileClip('CPU sigue vivo.mp4') 
                  clip.preview(fps=60, audio=False)
                  clip.close()
                  mostrar_mensaje(Texto_8, (0,0) )
                  mostrar_mensaje(Texto_9, (0,55))
          elif evento.key == K_x:
             dinero = 0
             objeto_ventana.blit(imagen_Quiebra, (0,0) )
             pygame.display.update()
             time.sleep(5)
             pygame.quit()                       #Que se cierre la ventana
             sys.exit()