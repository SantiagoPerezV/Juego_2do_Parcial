import pygame
from constantes import *
def armarAnimacion(path_parcial, cantidad, left, top) -> list:
    lista = []
    i = 0
    for i in range(cantidad):
        path = 'sprites\Walk_' + str(path_parcial) + 'panda_01_walk_' + str(i) + '.png'
        imagen_personaje = pygame.image.load(path)
        imagen_personaje = pygame.transform.scale(imagen_personaje, (130, 130)) #ancho, alto
        rect_imagen = imagen_personaje.get_rect()
        rect_imagen.x = left #margen left 100
        rect_imagen.y = top #margen top 430
        dic_personaje = {}
        dic_personaje["imagen"] = imagen_personaje
        dic_personaje["rect_personaje"] = rect_imagen
        lista.append(dic_personaje)
    return lista

class Personaje:
    def __init__(self, pathD, pathI, cantidad, direccion, left, top) -> None:
        self.lista_pasos_D = armarAnimacion (pathD, cantidad, left, top)
        self.lista_pasos_I = armarAnimacion(pathI, cantidad, left, top)
        self.direccion_actual = direccion
        self.pos_actual = left

    def girar(self, pos_fotograma, direccion, lista_pasos) -> int:
        for i in range(len(lista_pasos)):
            lista_pasos[i]["rect_personaje"].x = self.pos_actual

        self.direccion_actual = direccion
        if pos_fotograma < len(lista_pasos) - 1:
            pos_fotograma += 1
        else:
            pos_fotograma = 0

        return pos_fotograma
    
    def correr(self, pos_fotograma, lista_pasos, direccion) -> int:
        if direccion == DIRECCION_L:
            lista_pasos[pos_fotograma]["rect_personaje"].x -= 30
        else:
            lista_pasos[pos_fotograma]["rect_personaje"].x += 30

        self.pos_actual = lista_pasos[pos_fotograma]["rect_personaje"].x
        if pos_fotograma < len(lista_pasos) - 1:
            pos_fotograma += 1
        else:
            pos_fotograma = 0

        return pos_fotograma

    def actualizarPersonaje(self, pantalla, direccion, pos_fotograma):
        if direccion == DIRECCION_R:
            pantalla.blit(self.lista_pasos_D[pos_fotograma]["imagen"], self.lista_pasos_D[pos_fotograma]["rect_personaje"])
        else:
            pantalla.blit(self.lista_pasos_I[pos_fotograma]["imagen"], self.lista_pasos_I[pos_fotograma]["rect_personaje"])
