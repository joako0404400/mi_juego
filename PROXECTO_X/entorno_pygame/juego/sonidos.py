import pygame

pygame.mixer.init()
sonido_salto = pygame.mixer.Sound("entorno_pygame/juego/assets/el_salto_Del_papu.mp3")
musica_fondo = pygame.mixer.Sound("entorno_pygame/juego/assets/rap_de_los_puntos.mp3")
musica_fondo.play(-1)
sonido_perdida = pygame.mixer.Sound("entorno_pygame/juego/assets/perder.mp3")
sonido_laser = pygame.mixer.Sound("entorno_pygame/juego/assets/disparo.mp3")