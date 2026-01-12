'''JUEGO ARCADE PONG'''

import turtle
import time

class Paletas(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color('orange')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos,0)

    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 40)
    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 40)  

class Pelota(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0) 
        self.dx = 0.1
        self.dy = 0.1            

    def movimiento(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def rebote_y(self):
        self.dy *= -1

    def rebote_x(self):
        self.dx *= -1

    def posicion_inicial(self):
        self.goto(0,0)
        self.rebote_x()    

class Marcador(turtle.Turtle):
    def __init__(self):
        super().__init__()        
        self.marcador_izq = 0
        self.marcador_der = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_marcador()

    def update_marcador(self):
        self.clear()
        self.write(f'{self.marcador_izq}       {self.marcador_der}',
                   align='center', font=('Courier',24,'normal'))
        
    def puntos_izq(self):
        self.marcador_izq += 1
        self.update_marcador()

    def puntos_der(self):
        self.marcador_der += 1
        self.update_marcador()

    def mostrar_ganador(self, ganador):
        self.goto(0,90)
        self.write(
            f'¡{ganador} gana!', align='center', font= ('Arial', 40, 'bold')
        )    

class Game():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title('Pong POO by Maru')
        self.screen.bgcolor('purple')
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.paleta_izq = Paletas(-350)
        self.paleta_der = Paletas(350)
        self.pelota = Pelota()
        self.marcador = Marcador()

        self.screen.listen()
        self.screen.onkeypress(self.paleta_izq.up, 'w')
        self.screen.onkeypress(self.paleta_izq.down, 's')
        self.screen.onkeypress(self.paleta_der.up, 'Up')
        self.screen.onkeypress(self.paleta_der.down, 'Down')

    def contador_inicio(self):
     contador = turtle.Turtle()
     contador.hideturtle()
     contador.color("white")
     contador.penup()
     contador.goto(0, 0)

     for num in ["3", "2", "1", "¡YA!"]:
        contador.clear()
        contador.write(num, align="center", font=("Arial", 50, "bold"))
        self.screen.update()
        time.sleep(1)  

     contador.clear()
    

    def play(self):

        self.contador_inicio()

        while True:
            self.screen.update()
            self.pelota.movimiento()

            # Rebotes arriba/abajo
            if self.pelota.ycor() > 290 or self.pelota.ycor() < -290:
                self.pelota.rebote_y()

            # Punto para izquierda
            if self.pelota.xcor() > 390:
                self.marcador.puntos_izq()
                if self.marcador.marcador_izq == 5:
                    self.marcador.mostrar_ganador('Jugador izquierdo')
                    self.screen.update()
                    break
                self.pelota.posicion_inicial()

                # Punto para derecha
            if self.pelota.xcor() < -390:
                self.marcador.puntos_der()
                if self.marcador.marcador_der == 5:
                    self.marcador.mostrar_ganador("Jugador derecho")
                    self.screen.update()
                    break
                self.pelota.posicion_inicial()

                # Colisión con paleta izquierda
            if (-350 < self.pelota.xcor() < -330 and
                self.paleta_izq.ycor() -50 < self.pelota.ycor() < self.paleta_izq.ycor() +50):
                self.pelota.setx(-330)
                self.pelota.rebote_x()

                # Colisión con paleta derecha
            if (330 < self.pelota.xcor() < 350
                and self.paleta_der.ycor() - 50 < self.pelota.ycor() < self.paleta_der.ycor() + 50):
                self.pelota.setx(330)
                self.pelota.rebote_x()

        self.screen.mainloop()

# Ejecutando el juego
game = Game()
game.play() 
