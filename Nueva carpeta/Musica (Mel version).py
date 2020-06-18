# -*- coding: utf-8 -*-

import sys
import pygame

from pygame.locals import *  #Para inicializar todos los modulos que vienen con esa libreria
pygame.init()

def songselect(newsong, playingsong, pause):
  miFuente = pygame.font.SysFont("Arial", 30)
  if newsong != playingsong:
    pygame.mixer.music.load(newsong + ".mp3")
    pygame.mixer.music.play(-1)
    pause = False
  return newsong, miFuente.render("Reproduciendo: {}".format(newsong), 0, color_rojo), pause

def cambiar_volumen(sonido, cambio):
  sonido += cambio
  pygame.mixer.music.set_volume(sonido)
  pygame.time.delay(60)
  return pygame.mixer.music.get_volume()

objeto_ventana = pygame.display.set_mode((1300,600))  #Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("Hola soy una ventana")   #Titulo de la pantalla

color_negro = (0,0,0)
color_rojo = (255,0,0)

miFuente = pygame.font.SysFont("Arial", 30)
Texto_1 = miFuente.render("1) Jazz - Rap", 0, color_rojo)
Texto_2 = miFuente.render("2) Casino Night", 0, color_rojo)
Texto_3 = miFuente.render("3) Studiopolis", 0, color_rojo)
Texto_4 = miFuente.render("4) Mirage Saloon", 0, color_rojo)
Texto_5 = miFuente.render("5) Stardust Speedway", 0, color_rojo)
Texto_6 = miFuente.render("6) Chemical", 0, color_rojo)
Texto_7 = miFuente.render("Reproduciendo: Jazz - Rap",0,color_rojo)

pygame.mixer.music.load("Jazz - Rap.mp3")
newsong = "Jazz - Rap"
playingsong = newsong
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1.0)   
firsttime=True
themelist=["Jazz - Rap", "Casino Night", "Studiopolis", "Mirage Saloon", "Stardust Speedway", "Chemical"]
pause = False
sonido = pygame.mixer.music.get_volume()

while True:                   #Un while infinito para que no se cierre la ventana
    eventflag=False
    #Texto_8 = miFuente.render("Sonido: " + str("{0:.1f}".format(sonido*100)), 0, color_rojo)

    for evento in pygame.event.get():       #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
      if evento.type == QUIT:
        pygame.quit()             #Que se cierre la ventana
        sys.exit()
      elif evento.type == pygame.KEYDOWN:
        eventflag=True
        if evento.key == K_1: newsong = themelist[0]
        elif evento.key == K_2: newsong = themelist[1]
        elif evento.key == K_3: newsong = themelist[2]
        elif evento.key == K_4: newsong = themelist[3]
        elif evento.key == K_5: newsong = themelist[4]
        elif evento.key == K_6: newsong = themelist[5]
        elif evento.key == K_r: #Reiniciar tema
          newsong=playingsong
          playingsong=""
          playingsong, Texto_7, pause = songselect(newsong, playingsong, pause)
        elif evento.key == K_p: #Pausear/despausear tema
          pause = not pause
          if pause: pygame.mixer.music.pause()
          else: pygame.mixer.music.unpause()
        elif evento.key == K_RIGHT: #Pasar al tema siguiente
          if themelist.index(playingsong)+1 == len(themelist): newsong = themelist[0]
          else: newsong = themelist[themelist.index(playingsong)+1]
        elif evento.key == K_LEFT: newsong=themelist[themelist.index(playingsong)-1] #Pasar al tema anterior
        playingsong, Texto_7, pause = songselect(newsong, playingsong, pause)
    evento = pygame.key.get_pressed()
    if evento[pygame.K_UP]:
      eventflag=True
      sonido = cambiar_volumen(sonido, 0.01)
    if evento[pygame.K_DOWN]:
      eventflag=True
      sonido = cambiar_volumen(sonido, -0.01)
    if eventflag or firsttime:
      objeto_ventana.fill(color_negro)
      objeto_ventana.blit(Texto_1, (0, 0) )
      objeto_ventana.blit(Texto_2, (0, 30) )
      objeto_ventana.blit(Texto_3, (0, 60) )
      objeto_ventana.blit(Texto_4, (0, 90) )
      objeto_ventana.blit(Texto_5, (0, 120) )
      objeto_ventana.blit(Texto_6, (0, 150) )
      objeto_ventana.blit(Texto_7, (0, 210) )
      Texto_8 = miFuente.render("Sonido: " + str(int(sonido * 100)), 0, color_rojo)
      objeto_ventana.blit(Texto_8, (0, 240) )
      pygame.display.update() #Para que se actualize la pantalla
    firsttime=False

pygame.mixer.music.stop()