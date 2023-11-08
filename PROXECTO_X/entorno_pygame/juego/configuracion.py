import pygame
import random

# Configuración de la pantalla
ANCHO = 400
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El salto del papu")
FPS = 30 


# Colores
BLANCO = (255, 255, 255)

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Variables del juego
jugando = True

# Definir el pájaro
pajaro = pygame.Rect(50, ALTO // 2, 40, 40)
GRAVEDAD = 1
SALTO = -10
velocidad_pajaro = 0

# Definir la lista de tuberías
tuberias = []

# Otras configuraciones...
MAX_ENEMIGOS = 4  # Ajusta el número máximo de enemigos que deseas





# Función para crear una tubería
def crear_tuberia():
    espacio_vertical = random.randint(200, 400)  # Ajusta el espacio vertical entre las tuberías
    ancho_tubo = 80  # Ajusta el ancho deseado
    alto_tubo = espacio_vertical - 100  # Calcula la altura de la tubería superior
    tuberia_arriba = pygame.Rect(ANCHO, 0, ancho_tubo, alto_tubo)
    tuberia_abajo = pygame.Rect(ANCHO, espacio_vertical + 100, ancho_tubo, ALTO - espacio_vertical - 100)
    return (tuberia_arriba, tuberia_abajo)


# Función para crear una tubería
def crear_tuberia():
    espacio_vertical = random.randint(200, 400)  # Ajusta el espacio vertical entre las tuberías
    tuberia_arriba = pygame.Rect(ANCHO, 0, 80, espacio_vertical - 100)
    tuberia_abajo = pygame.Rect(ANCHO, espacio_vertical + 100, 80, ALTO - espacio_vertical - 100)
    return (tuberia_arriba, tuberia_abajo)

# Función para mover las tuberías
def mover_tuberias():
    for tuberia in tuberias:
        tuberia[0].x -= 5
        tuberia[1].x -= 5

# Función para dibujar las tuberías en la pantalla
def dibujar_tuberias():
    for tuberia in tuberias:
        pygame.draw.rect(PANTALLA, (0, 128, 0), tuberia[0])
        pygame.draw.rect(PANTALLA, (0, 128, 0), tuberia[1])

# Función para verificar colisiones
def verificar_colision():
    for tuberia in tuberias:
        if pajaro.colliderect(tuberia[0]) or pajaro.colliderect(tuberia[1]) or pajaro.y < 0 or pajaro.y > ALTO:
            return True
    return False

def crear_enemigo():
    # Genera una posición aleatoria en la parte derecha de la pantalla
    x = ANCHO
    y = random.randint(0, ALTO - 40)  # Ajusta la posición vertical según tus necesidades
    # Crea un rectángulo para representar al enemigo
    enemigo = pygame.Rect(x, y, 40, 40)
    return enemigo
# Función para mover los enemigos hacia el jugador
def mover_enemigos():
    for enemigo in enemigos:
        if enemigo.x < pajaro.x:
            enemigo.x += 5  # Mover hacia la derecha
        elif enemigo.x > pajaro.x:
            enemigo.x -= 5  # Mover hacia la izquierda
            
def manejar_colisiones_enemigos(vidas, enemigos):
    # Crear una nueva lista de enemigos que no colisionaron con el pájaro
    enemigos_no_colisionados = [enemigo for enemigo in enemigos if not pajaro.colliderect(enemigo)]

    # Comprobar si un enemigo ha salido de la pantalla y crear uno nuevo en su lugar
    for enemigo in enemigos_no_colisionados:
        if enemigo.right < 0:
            enemigos_no_colisionados.remove(enemigo)  # Eliminar el enemigo
            enemigos_no_colisionados.append(crear_enemigo())  # Crear un nuevo enemigo

    return len(enemigos_no_colisionados)        

# Función para crear un enemigo fuerte
def crear_enemigo_fuerte():
    x = ANCHO
    y = random.randint(0, ALTO - 40)  # Ajusta la posición vertical según tus necesidades
    # Puedes personalizar el enemigo fuerte aquí (por ejemplo, más grande, más rápido, etc.)
    enemigo_fuerte = pygame.Rect(x, y, 60, 60)  # Ejemplo de un enemigo más grande
    return enemigo_fuerte