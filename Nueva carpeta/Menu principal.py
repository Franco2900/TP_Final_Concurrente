import sys
import os
import inspect
import pygame
import subprocess 

from pygame.locals import *  #Para inicializar todos los modulos que vienen con esa libreria
pygame.init()

def cambiar_volumen(cambio):
  sonido += cambio
  pygame.mixer.music.set_volume(sonido)
  pygame.time.delay(60)

def end():
  pygame.quit()             #Que se cierre la ventana
  sys.exit()

objeto_ventana = pygame.display.set_mode((800,600))  #Tamaño de la ventana (Ancho/Alto)
pygame.display.set_caption("Hola soy una ventana")   #Titulo de la pantalla

color_negro = (0,0,0)
color_rojo = (255,0,0)

dinero = 150

miFuente = pygame.font.SysFont("Arial", 30)
Texto_0 = miFuente.render("0) Salir", 0, color_rojo)
Texto_1 = miFuente.render("1) Maquina Tragamonedas", 0, color_rojo)
Texto_2 = miFuente.render("2) Veintiuno", 0, color_rojo)
Texto_3 = miFuente.render("3) Ruleta", 0, color_rojo)
Texto_4 = miFuente.render("4) Domino", 0, color_rojo)
Texto_5 = miFuente.render("5) Ruleta Rusa", 0, color_rojo)
Texto_6 = miFuente.render("6) Reproductor", 0, color_rojo)
Texto_7 = miFuente.render("Dinero: {}".format(dinero), 0, color_rojo)

while True:                   #Un while infinito para que no se cierre la ventana
  objeto_ventana.fill(color_negro)
  objeto_ventana.blit(Texto_0, (0, 0) )
  objeto_ventana.blit(Texto_1, (0, 30) )
  objeto_ventana.blit(Texto_2, (0, 60) )
  objeto_ventana.blit(Texto_3, (0, 90) )
  objeto_ventana.blit(Texto_4, (0, 120) )
  objeto_ventana.blit(Texto_5, (0, 150) )
  objeto_ventana.blit(Texto_6, (0, 180) )
  objeto_ventana.blit(Texto_7, (0, 240) )
  pygame.display.update() #Para que se actualize la pantalla

  for evento in pygame.event.get():       #Se indica que se fije los resultados de los eventos (como cerrar una ventana o imprimir un mensaje)
    if evento.type == QUIT: end()
    elif evento.type == pygame.KEYDOWN:
      if evento.key == K_0: end()        
      elif evento.key == K_1:
        """script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "Maquina Tragamonedas/" + "Maquina tragamonedas (Mel version)"
        abs_file_path = os.path.join(script_dir, rel_path)
        import abs_file_path"""
        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        currentdir = os.path.join(currentdir, "Maquina Tragamonedas/")
        parentdir = os.path.dirname(currentdir)
        sys.path.insert(0,parentdir)
        print(sys.path)
        input()
        import Maquina_tragamonedas.py

      #elif evento.key == K_2: commands.getoutput('Proyectos con Git/TP_Final_Concurrente/Ruleta Casino.py')
      elif evento.key == K_2: subprocess.call('Proyectos con Git/TP_Final_Concurrente/Ruleta Casino.py', shell=True)
      elif evento.key == K_3: pass
      elif evento.key == K_4: pass
      elif evento.key == K_5: pass
      elif evento.key == K_6: subprocess.call('Musica (Mel version).py', shell=True)

pygame.mixer.music.stop()