from constantes import *
from objetos_juego import *
import pygame
pos_fotograma = 0

panda = Personaje('Right\\', 'Left\\', 4, DIRECCION_R, 100, 430)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('MI JUEGO')
reloj = pygame.time.Clock()

flag_correr = True
while flag_correr:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_correr = False

    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            if panda.direccion_actual == DIRECCION_L:
            #si antes venia de correr a la derecha venia de la izquierda
                pos_fotograma = panda.girar(pos_fotograma, DIRECCION_L, panda.lista_pasos_D)
            else:
                #si sus pasos venían en la misma dirección
                pos_fotograma = panda.correr(pos_fotograma, panda.lista_pasos_D, DIRECCION_R)
                
        if lista_teclas[pygame.K_LEFT]:
            if panda.direccion_actual == DIRECCION_R:
                #si antes venia de correr a la izquierda venia de la derecha
                pos_fotograma = panda.girar(pos_fotograma, DIRECCION_R, panda.lista_pasos_I)
            else:
                #si sus pasos venían en la misma dirección
                pos_fotograma = panda.correr(pos_fotograma, panda.lista_pasos_I, DIRECCION_L)

    milis = reloj.tick(20)

    pantalla.fill(COLOR_AZUL)

    panda.actualizarPersonaje(pantalla, panda.direccion_actual, pos_fotograma)    

    pygame.display.flip()
    
pygame.quit