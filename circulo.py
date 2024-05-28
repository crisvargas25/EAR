import turtle

class TicTacToeCircle:
    def __init__(self, size=200):
        self.size = size // 3  # Tamaño ajustado al tamaño del tablero
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()

    def draw_circle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.circle(self.size // 2)
        
    def display(self):
        screen = turtle.Screen()
        screen.mainloop()


# Ejemplo de uso
circle = TicTacToeCircle(300)

circle.display()
