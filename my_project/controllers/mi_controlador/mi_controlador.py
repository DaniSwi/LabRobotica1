from controller import Robot, Keyboard
import random

robot = Robot()
teclado = Keyboard()
teclado.enable(int(robot.getBasicTimeStep()))

timestep = int(robot.getBasicTimeStep())

#configurar motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

#establecer posición inicial en infinito (necesario para modo velocidad)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

#velocidad base
#MAX_VEL = 6.28

"""#movimiento recto primero
vl = 3.0
vr = -3.0

left_motor.setVelocity(vl)
right_motor.setVelocity(vr) """

"""
nota del funcionamiento del código:
se tiene que mantener la tecla para que el robot
haga el movimiento, por ejemplo
para que vaya recto hay que 
mantener la tecla J.
"""

L = 0.052 #distancia entre las ruedas del e-puck en metros

while robot.step(timestep) != -1:
    tecla = teclado.getKey()
    v = 0.0
    w = 0.0
    
    #si aprieta J va recto
    if tecla == ord("J"):
        v = 0.1
        w = 0.0
    #si aprieta L es una curva a la izquierda
    elif tecla == ord("L"):
        v = 0.05
        w = 0.5
    #si aprieta R es una curva a la derecha
    elif tecla == ord("R"):
        v = 0.05 
        w = -0.5
    elif tecla == ord("O"):
        v = 0.0
        w = 2.0
    #extra de realizar una trayectoria de circulo de radio 0.2
    elif tecla == ord("C"):
        v = 0.1
        w = v/0.2 #circulo de radio 0.2m w = v/R
    #extra agregación de bias, ejemplo motor derecho es un 3% más lento que 
    #el otro motor izquierdo
    bias_der = 0.97
        
    vr = v + (w * L) / 2
    vl = v - (w * L) / 2
    
    vr = vr * bias_der
    
    #ruido aleatorio (extra)
    ruido = random.uniform(-0.01, 0.01)
    vl = vl + ruido
    
    #conversion de m/s a rad/s+
    r = 0.0205
        
    left_motor.setVelocity(vl/r)
    right_motor.setVelocity(vr/r)
    
    print("Velocidad derecha = ", vr)
    print("Velocidad izquierda =", vl)
