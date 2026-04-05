from controller import Robot, Keyboard

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
MAX_VEL = 6.28

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

while robot.step(timestep) != -1:
    tecla = teclado.getKey()
    vl = 0.0
    vr = 0.0
    
    #si aprieta J va recto
    if tecla == ord("J"):
        vl = 3.0
        vr = 3.0
    #si aprieta L es una curva a la izquierda
    elif tecla == ord("L"):
        vl = 1.0
        vr = 4.0
    #si aprieta R es una curva a la derecha
    elif tecla == ord("R"):
        vl = 4.0
        vr = 1.0
    elif tecla == ord("O"):
        vl = 3.0
        vr = -3.0
        
    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)
    
    print("Velocidad derecha = ", vr)
    print("Velocidad izquierda =", vl)