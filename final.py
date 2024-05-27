import turtle

class TicTacToeGame:
    def __init__(self, size=300):
        self.size = size
        self.cell_size = size // 3
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)  # Configura la velocidad de la tortuga a la más rápida
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.moves_count = 0
        self.setup_screen()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Juego de Tres en Raya")
        self.screen.setup(width=self.size + 100, height=self.size + 100)
        self.screen.setworldcoordinates(-self.size//2, -self.size//2, self.size//2, self.size//2)
        self.screen.onclick(self.handle_click)
        self.draw_board()

    def draw_board(self):
        self.turtle.penup()
        for i in range(1, 3):
            self.turtle.goto(-self.size//2, self.size//2 - i * self.cell_size)
            self.turtle.pendown()
            self.turtle.goto(self.size//2, self.size//2 - i * self.cell_size)
            self.turtle.penup()

        self.turtle.goto(-self.size//2, self.size//2)
        self.turtle.right(90)
        for i in range(1, 3):
            self.turtle.goto(-self.size//2 + i * self.cell_size, self.size//2)
            self.turtle.pendown()
            self.turtle.goto(-self.size//2 + i * self.cell_size, -self.size//2)
            self.turtle.penup()

        self.turtle.right(90)  # Restablece la dirección de la tortuga

    def draw_x(self, center_x, center_y):
        self.turtle.penup()
        self.turtle.goto(center_x - self.cell_size//3, center_y + self.cell_size//3)
        self.turtle.pendown()
        self.turtle.goto(center_x + self.cell_size//3, center_y - self.cell_size//3)
        self.turtle.penup()
        self.turtle.goto(center_x + self.cell_size//3, center_y + self.cell_size//3)
        self.turtle.pendown()
        self.turtle.goto(center_x - self.cell_size//3, center_y - self.cell_size//3)
        self.turtle.penup()

    def draw_circle(self, center_x, center_y):
        self.turtle.penup()
        self.turtle.goto(center_x + self.cell_size//10, center_y - self.cell_size//3)
        self.turtle.setheading(0)  # Asegura que el círculo se dibuje en la orientación correcta
        self.turtle.pendown()
        self.turtle.circle(self.cell_size//3)
        self.turtle.penup()

    def handle_click(self, x, y):
        if self.moves_count >= 9:
            return
        
        col = int((x + self.size // 2) // self.cell_size)
        row = int((self.size // 2 - y) // self.cell_size)
        
        if 0 <= col < 3 and 0 <= row < 3 and self.board[row][col] == '':
            self.board[row][col] = self.current_player
            center_x = col * self.cell_size - self.size // 2 + self.cell_size // 2
            center_y = self.size // 2 - row * self.cell_size - self.cell_size // 2
            if self.current_player == 'X':
                self.draw_x(center_x, center_y)
            else:
                self.draw_circle(center_x, center_y)
            
            self.moves_count += 1

            if self.check_winner(row, col):
                self.screen.title(f"Jugador {self.current_player} gana!")
                self.screen.onclick(None)  # Desactiva más clics
            elif self.check_tie():
                self.screen.title("¡Es un empate!")
                self.screen.onclick(None)  # Desactiva más clics
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Verifica fila
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Verifica columna
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Verifica diagonal
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Verifica diagonal inversa
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))

    def display(self):
        self.screen.mainloop()

# Uso de la clase para iniciar el juego de tres en raya
game = TicTacToeGame(300)
game.display()