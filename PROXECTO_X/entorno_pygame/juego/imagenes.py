import pygame
from configuracion import ANCHO, ALTO

fondo = pygame.image.load("entorno_pygame/juego/assets/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
pajaro_imagen = pygame.image.load("entorno_pygame/juego/assets/pajaro.png")
pajaro_imagen = pygame.transform.scale(pajaro_imagen, (50, 50))
enemigo1_imagen = pygame.image.load("entorno_pygame/juego/assets/enemigo1.png")
enemigo2_imagen = pygame.image.load("entorno_pygame/juego/assets/enemigo2.png")
enemigo1_imagen = pygame.transform.scale(enemigo1_imagen, (50, 50))
enemigo2_imagen = pygame.transform.scale(enemigo2_imagen, (50, 50))