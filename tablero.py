import turtle
from abc import ABC

class Grafico(ABC):
    def dibujar(self, turtle):
        pass

class TicTacToeBoard:
    def __init__(self, size):
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.graficos = []

    def add_grafico(self, grafico):
        self.graficos.append(grafico)

    def draw_board(self):
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, -self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 6, self.size // 2)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(self.size // 6, self.size // 2)
        self.turtle.pendown()
        self.turtle.forward(self.size)

    def draw_graficos(self):
        for grafico in self.graficos:
            grafico.dibujar(self.turtle)

    def display(self):
        screen = turtle.Screen()
        self.draw_board()
        self.draw_graficos()
        screen.mainloop()

class Equis(Grafico):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self, turtle):
        equis = 160
        turtle.penup()
        turtle.goto(self.x - equis // 2, self.y + equis // 2)
        turtle.pendown()
        turtle.goto(self.x + equis // 2, self.y - equis // 2)

        turtle.penup()
        turtle.goto(self.x - equis // 2, self.y - equis // 2)
        turtle.pendown()
        turtle.goto(self.x + equis // 2, self.y + equis // 2)
        turtle.penup()

class Circulo(Grafico):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self, turtle):
        radio = 100
        turtle.speed(10)
        turtle.penup()
        turtle.goto(self.x, self.y - radio - 100)
        turtle.pendown()
        turtle.circle(radio)
        turtle.penup()

# Ejemplo de uso
board = TicTacToeBoard(800)
board.add_grafico(Equis(0, 0))
board.add_grafico(Circulo(200, 200))
board.display()
