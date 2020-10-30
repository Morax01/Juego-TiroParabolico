#Importación de las librerias
from random import randrange
from turtle import *
from freegames import vector

#Integrantes del equipo:
# 
# Isaac Arredondo Padrón | A00828359

# Inicializador de los vectores de las pelotas rojas y azules
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Función que inicializa la velocidad de la pelota roja en respuesta a la posición de los clicks del cursor
def tap(x, y):
    # Responder al toque de la pantalla.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# Verifica si el tap se encuentra dentro de la ventana
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200
# Dibujar pelota y objetivos.
def draw():
    
    clear()
    # Dibuja los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    # Dibuja la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()
# Mueve la pelota y los objetivos
def move():
    # Da la posición a los objetivos
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    # Cambia la posicion de los objetivos
    for target in targets:
        target.x -= 0.5
    # Cambia la posicion del proyectil
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    # Hace un copiado del vector de los orbes azules para mantener un control
    dupe = targets.copy()
    targets.clear()
    # Vector que se encarga guardar la posicion de los objetivos
    #que no han sido eliminados
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    # Llamando a la funcion para dibujar
    draw()
    # Se reposicionan los targets al tocar la pared
    for target in targets:
        if not inside(target):
            return
    #Cambiamos la velocidad
    ontimer(move, 10)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
