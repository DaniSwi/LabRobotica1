from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

#configurar motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

#establecer posición inicial en infinito (necesario para modo velocidad)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

#movimiento recto primero
vl = 3.0
vr = -3.0

left_motor.setVelocity(vl)
right_motor.setVelocity(vr)

while robot.step(timestep) != -1:
    print("Velocidad derecha = ", vr)
    print("Velocidad izquierda =", vl)