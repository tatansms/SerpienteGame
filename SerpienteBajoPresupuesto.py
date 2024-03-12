import turtle
import time
import random

##Juego hecho por el youtuber YouDesv
##https://www.youtube.com/watch?v=lKzEvbGbbPo&t=9s

class SnakeGame:
  def __init__(self):
    self.posponer = 0.1
    self.score = 0
    self.high_score = 0

    self.wn = turtle.Screen()
    self.wn.title("Snake Game 1.5.2")
    self.wn.bgcolor("black")
    self.wn.setup(width=600, height=600)
    self.wn.tracer(0)

    self.cabeza = Snake()
    self.comida = Food()
    self.segmentos = []

    self.texto = turtle.Turtle()
    self.texto.speed(0)
    self.texto.color("white")
    self.texto.penup()
    self.texto.hideturtle()
    self.texto.goto(0, 260)
    self.actualizar_puntaje()

    self.configurar_teclado()

    
  def configurar_teclado(self):
    self.wn.listen()
    self.wn.onkeypress(self.cabeza.arriba, "Up")
    self.wn.onkeypress(self.cabeza.abajo, "Down")
    self.wn.onkeypress(self.cabeza.izquierda, "Left")
    self.wn.onkeypress(self.cabeza.derecha, "Right")

  def actualizar_puntaje(self):
    self.texto.clear()
    self.texto.write(f"Score: {self.score}     High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

  def jugar(self):
    while True:
      self.wn.update()
      self.cabeza.mover()
      self.colisiones_bordes()
      self.colisiones_comida()
      self.colisiones_cuerpo()
      # Mueve los segmentos siguiendo a la cabeza
      for i in range(len(self.segmentos) - 1, 0, -1):
        x = self.segmentos[i - 1].xcor()
        y = self.segmentos[i - 1].ycor()
        self.segmentos[i].goto(x, y)
      if len(self.segmentos) > 0:
        x = self.cabeza.xcor()
        y = self.cabeza.ycor()
        self.segmentos[0].goto(x, y)
      time.sleep(self.posponer)

  def colisiones_bordes(self):
    if self.cabeza.xcor() > 280 or self.cabeza.xcor() < -280 or self.cabeza.ycor() > 280 or self.cabeza.ycor() < -280:
      self.resetear_juego()

  def colisiones_comida(self):
    if self.cabeza.distance(self.comida) < 20:
      self.comida.reubicar()
      self.score += 1
      if self.score > self.high_score:
        self.high_score = self.score
      self.actualizar_puntaje()
      self.crear_segmento()

  def colisiones_cuerpo(self):
    for segmento in self.segmentos:
      if segmento.distance(self.cabeza) < 20:
        self.resetear_juego()

  def crear_segmento(self):
    nuevo_segmento = Snake()
    self.segmentos.append(nuevo_segmento )

  def resetear_juego(self):
    time.sleep(1)
    self.cabeza.goto(0, 0)
    self.cabeza.direction = "stop"
    for segmento in self.segmentos:
      segmento.goto(1000, 1000)
    self.segmentos.clear()
    self.score = 0
    self.actualizar_puntaje()
    
    
   

class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.direction = "stop"
    
    def arriba(self):
        if self.direction != "down":
            self.direction = "up"
    
    def abajo(self):
        if self.direction != "up":
            self.direction = "down"
    
    def izquierda(self):
        if self.direction != "right":
            self.direction = "left"
    
    def derecha(self):
        if self.direction != "left":
            self.direction = "right"
    
    def mover(self):
        if self.direction == "up":
            self.sety(self.ycor() + 20)
        elif self.direction == "down":
            self.sety(self.ycor() - 20)
        elif self.direction == "left":
            self.setx(self.xcor() - 20)
        elif self.direction == "right":
            self.setx(self.xcor() + 20)

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 100)
    
    def reubicar(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

if __name__ == "__main__":
    juego = SnakeGame()
    juego.jugar()
