# LabRobotica1

## Laboratorio 1 de la asignatura Robótica y Sistemas Autónomos (ICI4150)

**Realizado por:**

- Daniel Cornejo
- Ian Guerrero
- Isidora Osorio

## Descripción

Este proyecto consiste en la simulación de un robot **e-puck** en el entorno **Webots**. Se implementa un modelo de control cinemático diferencial donde el movimiento del robot es determinado por las velocidades independientes de sus dos ruedas motrices

## Objetivos

  * Comprender el comportamiento cinemático de un robot diferencial mediante simulación interactiva
  * Implementar el control de actuadores (motores) mediante programación en **Python** en el entorno de **Webots**
  * Analizar la relación entre las velocidades de las ruedas y las trayectorias resultantes (rectas, curvas y rotación)

## Modelo Cinemático

El control se basa en las siguientes ecuaciones fundamentales extraídas del laboratorio

  * **Velocidad Lineal ($v$):** $v = \frac{v_r + v_l}{2}$
  * **Velocidad Angular ($\omega$):** $\omega = \frac{v_r - v_l}{L}$

Donde:

  * $v_r$: Velocidad de la rueda derecha
  * $v_l$: Velocidad de la rueda izquierda
  * $L$: Distancia entre las ruedas (para el e-puck $L = 0.052$ m)

## Instrucciones de Ejecución

1.  **Instalación**: Asegúrese de tener instalado **Webots 2023** o superior y **Python 3.x**.
2.  **Carga del Mundo**: Abra el archivo ubicado en la carpeta `/worlds/laboratorio1.wbt`.
3.  **Configuración del Controlador**:
      * El robot e-puck ya tiene asignado el controlador `mi_controlador.py`.
      * Asegúrese de que la consola de Webots no muestre errores de ruta.
4.  **Interacción**: Haga clic en la ventana 3D y use las siguientes teclas para experimentar:
      * `J`: Movimiento Recto ($v_r = v_l$).
      * `L` / `R`: Trayectoria Curva ($v_r \neq v_l$).
      * `O`: Rotación en el lugar ($v_r = -v_l$).

## Código del Controlador (Python)

```python
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

    #calculo de velocidades de las ruedas por formula cinemática diferencial    
    vr = v + (w * L) / 2
    vl = v - (w * L) / 2
    
    #conversion de m/s a rad/s
    r = 0.0205
        
    #seteamos las velocidades a los motores
    left_motor.setVelocity(vl/r)
    right_motor.setVelocity(vr/r)
    
    print("Velocidad derecha = ", vr)
    print("Velocidad izquierda =", vl)
```

## Resultados y Análisis

| Experimento | Condición de Velocidad | Trayectoria Observada |
| :--- | :--- | :--- |
| **Recto** | $v_r = v_l$ | El robot avanza en el eje X local sin desviaciones. |
| **Curva** | $v_r > v_l$ | El robot describe un arco hacia la izquierda. |
| **Rotación** | $v_r = -v_l$ | El robot gira sobre su propio eje ($v=0$). |

### Preguntas de Análisis

1.  **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
   El robot mantiene una orientación constante y su velocidad angular $\omega$ es cero, resultando en una línea recta
2.  **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
   Se genera un momento de rotación que obliga al robot a seguir una trayectoria curva cuyo radio depende de la diferencia de velocidad
3.  **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?**
   El robot rota sobre su propio eje, permitiendo cambios de dirección rápidos sin desplazamiento lineal

-----
