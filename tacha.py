import turtle

class TicTacToeBoard:
    def __init__(self, size=200):
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()

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

    def display(self):
        screen = turtle.Screen()
        self.draw_board()

        # Dibujar un círculo en el centro
        circle = TicTacToeCircle(self.size)
        circle.draw_circle(0, 0)

        # Dibujar una tacha en la esquina superior izquierda
        cross = TicTacToeCross(self.size)
        cross.draw_cross(-self.size // 3, self.size // 3)

        screen.mainloop()

# Uso del tablero con los símbolos
board = TicTacToeBoard(300)
board.display()
