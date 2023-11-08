import pygame
import random
from configuracion import *

# Inicializar Pygame
pygame.init()

# Lista de láseres
lasers = []

# Inicializar el contador de puntos
puntuacion = 0

# Lista para llevar un registro de las tuberías ya pasadas
tuberias_pasadas = []

# Contador de vidas
vidas = 3  # Establece el número inicial de vidas

enemigos = []  # Lista para llevar un registro de los enemigos

# Contador de enemigos matados
enemigos_matados = 0

while jugando and vidas > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidad_pajaro = SALTO
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Botón derecho (3)
            # Agregar un láser a la lista
            nuevo_laser = {"x": pajaro.x, "y": pajaro.y, "velocidad": 10}
            lasers.append(nuevo_laser)

    # Mover el pájaro
    velocidad_pajaro += GRAVEDAD
    pajaro.y += velocidad_pajaro

    # Crear nuevas tuberías y eliminar las antiguas
    if len(tuberias) == 0 or tuberias[-1][0].x < ANCHO - 200:
        tuberias.append(crear_tuberia())
        if len(tuberias) > 3:
            del tuberias[0]

    # Mover y dibujar las tuberías
    mover_tuberias()

    # Verificar colisiones con las tuberías
    if verificar_colision():
        vidas -= 1  # Restar una vida
        if vidas > 0:
            velocidad_pajaro = 0
            tuberias = []
            # Limpiar la lista de tuberías pasadas
            tuberias_pasadas = []

    # Verificar colisiones entre el jugador y los enemigos
    for enemigo in enemigos:
        if pygame.Rect(pajaro).colliderect(enemigo):
            vidas -= 1  # Restar una vida
            enemigos.remove(enemigo)  # Eliminar el enemigo

    # Verificar si se ha pasado una tubería y aún no se ha registrado
    for tuberia in tuberias:
        if tuberia[0].right < pajaro.left and tuberia not in tuberias_pasadas:
            puntuacion += 1
            tuberias_pasadas.append(tuberia)

    # Lógica para los enemigos
    if len(enemigos) < MAX_ENEMIGOS:  # Ajusta el número máximo de enemigos que deseas
        enemigos.append(crear_enemigo())

    for enemigo in enemigos:
        enemigo.x -= 10  # Mover enemigos hacia la izquierda

    # Comprobar si un enemigo ha salido de la pantalla
    for enemigo in enemigos:
        if enemigo.right < 0:
            enemigos.remove(enemigo)  # Eliminar el enemigo
            enemigos.append(crear_enemigo())  # Crear un nuevo enemigo

    # Verificar colisiones entre los láseres y los enemigos
    lasers_a_eliminar = []  # Lista para almacenar láseres a eliminar
    enemigos_a_eliminar = []  # Lista para almacenar enemigos a eliminar

    for laser in lasers:
        for enemigo in enemigos:
            if pygame.Rect(laser['x'], laser['y'], 10, 2).colliderect(enemigo):
                lasers_a_eliminar.append(laser)
                enemigos_a_eliminar.append(enemigo)

    # Incrementar el contador de enemigos matados
    enemigos_matados += len(enemigos_a_eliminar)

    # Eliminar los láseres y enemigos que colisionaron
    for laser in lasers_a_eliminar:
        lasers.remove(laser)
    for enemigo in enemigos_a_eliminar:
        enemigos.remove(enemigo)

    # Dibujar el fondo
    PANTALLA.fill(BLANCO)

    # Dibujar las tuberías
    dibujar_tuberias()

    # Dibujar el pájaro
    pygame.draw.rect(PANTALLA, (255, 0, 0), pajaro)

    # Dibujar los láseres
    for laser in lasers:
        laser["x"] += laser["velocidad"]
        pygame.draw.rect(PANTALLA, (255, 0, 0), (laser['x'], laser['y'], 10, 2))

    # Dibujar los enemigos
    for enemigo in enemigos:
        pygame.draw.rect(PANTALLA, (0, 0, 255), enemigo)

    # Dibujar la puntuación en la parte superior de la pantalla
    fuente = pygame.font.Font(None, 36)
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 0))
    PANTALLA.blit(texto_puntuacion, (10, 10))

    # Dibujar el contador de vidas en la parte superior de la pantalla
    fuente_vidas = pygame.font.Font(None, 36)
    texto_vidas = fuente_vidas.render(f"Vidas: {vidas}", True, (0, 0, 0))
    PANTALLA.blit(texto_vidas, (ANCHO - 120, 10))

    # Dibujar el contador de enemigos matados en la parte inferior de la pantalla
    fuente_enemigos = pygame.font.Font(None, 24)
    texto_enemigos = fuente_enemigos.render(f"Enemigos Matados: {enemigos_matados}", True, (0, 0, 0))
    PANTALLA.blit(texto_enemigos, (10, ALTO - 30))

    pygame.display.update()
    reloj.tick(30)

# Game over: Mostrar el mensaje de Game Over
fuente_game_over = pygame.font.Font(None, 36)
texto_game_over = fuente_game_over.render(f"Game Over - Puntuación: {puntuacion}", True, (255, 0, 0))
PANTALLA.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO // 2 - texto_game_over.get_height() // 2))

# Mostrar el contador de enemigos matados debajo del mensaje de Game Over
fuente_enemigos_game_over = pygame.font.Font(None, 24)
texto_enemigos_game_over = fuente_enemigos_game_over.render(f"Enemigos Matados: {enemigos_matados}", True, (255, 0, 0))
PANTALLA.blit(texto_enemigos_game_over, (ANCHO // 2 - texto_enemigos_game_over.get_width() // 2, ALTO // 2 + 20))

pygame.display.update()

# Esperar unos segundos antes de salir
pygame.time.delay(3000)  # 3000 milisegundos (3 segundos)

pygame.quit()
