import turtle

class TicTacToeBoard:
    def __init__(self, size):
        self.size = size
        self.speed=(1009990)
        self.turtle = turtle.Turtle()

    def draw_board(self):
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, self.size // 6)
        self.turtle.pendown()
        self.speed=(1009999)
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, -self.size // 6)
        self.turtle.pendown()
        self.speed=(10099)
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 6, self.size // 2)
        self.turtle.right(90)
        self.turtle.pendown()
        self.speed=(100)
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(self.size // 6, self.size // 2)
        self.turtle.pendown()
        self.speed=(100)
        self.turtle.forward(self.size)

    def display(self):
        screen = turtle.Screen()
        self.draw_board()
        self.speed=(100)
        screen.mainloop()

# class circulo:
#     def dibujarCirculo(self, x, y):
#         if tortuga is None:
#             self.t = turtle.Turtle()
#         else:
#             self.t = tortuga
    
#         self.turtle.penup()
#         self.turtle.goto(self.size // 2, self.size // 6)
#         self.turtle.pendown()
#         self.turtle.circle(self.size // 2)

        




# circle = circulo()
board = TicTacToeBoard(800)
board.display()
