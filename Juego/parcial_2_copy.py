from constantes import *
from ClasePersonaje import *
import pygame

lista_correr_right = []
for i in range(8):
    path = 'run_right/run_right_' + str(i) + '.png'
    imagen_personaje = pygame.image.load(path)
    imagen_personaje = pygame.transform.scale(imagen_personaje, (80, 100)) #ancho, alto
    rect_imagen = imagen_personaje.get_rect()
    rect_imagen.x = 100 #margen left 100
    rect_imagen.y = 430 #margen top 430
    dic_personaje = {}
    dic_personaje["imagen"] = imagen_personaje
    dic_personaje["rect_personaje"] = rect_imagen
    lista_correr_right.append(dic_personaje)

lista_correr_left = []
for i in range(8):
    path = 'run_left/run_left_' + str(i) + '.png'
    imagen_personaje = pygame.image.load(path)
    imagen_personaje = pygame.transform.scale(imagen_personaje, (80, 100)) #ancho, alto
    rect_imagen = imagen_personaje.get_rect()
    rect_imagen.x = 100 #margen left 100
    rect_imagen.y = 430 #margen top 430
    dic_personaje = {}
    dic_personaje["imagen"] = imagen_personaje
    dic_personaje["rect_personaje"] = rect_imagen
    lista_correr_left.append(dic_personaje)

pos_fotograma = 0

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('MI JUEGO')
reloj = pygame.time.Clock()

direccion = DIRECCION_R
pos_actual = rect_imagen

flag_correr = True
while flag_correr:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_correr = False

    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            direccion = DIRECCION_R
            imagen_personaje = lista_correr_right[pos_fotograma]["imagen"]
            pos_fotograma += 1
            rect_imagen.x += 10
            pos_actual = rect_imagen
            if pos_fotograma > 7:
                pos_fotograma = 0
                
        if lista_teclas[pygame.K_LEFT]:
            direccion = DIRECCION_L
            imagen_personaje = lista_correr_left[pos_fotograma]["imagen"]
            pos_fotograma += 1
            rect_imagen.x -= 10
            pos_actual = rect_imagen
            if pos_fotograma > 7:
                pos_fotograma = 0

    milis = reloj.tick(20)

    pantalla.fill(COLOR_AZUL)
    pantalla.blit(imagen_personaje, (pos_actual))

    pygame.display.flip()
    
pygame.quit