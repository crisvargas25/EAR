import turtle

t= turtle.Turtle()
turtle.bgcolor('black')
t.speed(90909090909)
t.color("white")
pantalla=turtle.Screen()

# t.speed(1000)
# colors = ['red','dark red']
# for number in range (400):
#     t.forward(number+1)
#     t.right(89)
#     t.pencolor(colors[number%2])

t.penup()
t.home()
t.pensize(5)
t.color("white")


condiciones_ganadoras = [
            [(0, 0), (0, 1), (0, 2)],  
            [(1, 0), (1, 1), (1, 2)],  
            [(2, 0), (2, 1), (2, 2)], 
            [(0, 0), (1, 0), (2, 0)], 
            [(0, 1), (1, 1), (2, 1)],  
            [(0, 2), (1, 2), (2, 2)], 
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]  
        ]
jugadas_ambos=[]
jugadas_x=[]
jugadas_o=[]

tamaño= 800
celdaT=tamaño//3
jugador_x = True

class graficos():
    def __init__(self, t):
        self.t = t
        pass

    def dibujar_tablero(self, tamaño):
        t = self.t

        #dibujar lineas tablero horizontales
        t.penup()
        t.goto(-tamaño//2, tamaño//6)
        t.pendown()
        t.forward(tamaño)

        t.penup()
        t.goto(-tamaño//2, -tamaño//6)
        t.pendown()
        t.forward(tamaño)

        t.right(90)

        t.penup()
        t.goto(-tamaño//6, tamaño//2)
        t.pendown()
        t.forward(tamaño)

        t.penup()
        t.goto(tamaño//6, tamaño//2)
        t.pendown()
        t.forward(tamaño)
        t.penup()
        t.home()


    def dibujar_equis(self, x,y):
        t = self.t
        equis=160
        t.goto(x -equis//2, y + equis//2)
        t.pendown()
        t.goto(x + equis//2, y -equis//2)

        t.penup()
        t.goto(x -equis//2,y -equis//2)
        t.pendown()
        t.goto(x+equis//2, y+ equis//2)
        t.penup()


    def dibujar_circulo(self,x,y):
        t = self.t
        radio=100
        t.speed(10)
        t.penup()
        t.goto(x,y -radio)
        t.pendown()
        t.circle(radio)
        t.penup()

    def dibujar_linea_ganadora(condicion):
        x1, y1= condicion[0]
        x2, y2=condicion[-1]

        c_inicial_x= - tamaño// 2 + x1 * celdaT + celdaT//2
        c_inicial_y= - tamaño// 2 + y1 * celdaT + celdaT//2
        c_final_x= -tamaño//2 + x2 * celdaT + celdaT//2
        c_final_y= -tamaño//2 + y2 * celdaT + celdaT//2

        t.penup()
        t.color("yellow")
        t.pensize(5)
        t.goto(c_inicial_x,c_inicial_y)
        t.pendown()
        t.goto(c_final_x,c_final_y)
        t.penup()
        t.color()
        t.pensize()




def evitar_iguales(cell_x, cell_y):
    return (cell_x, cell_y) in jugadas_ambos

def comprobar_ganador(jugadas):
    for condicion in condiciones_ganadoras:
        if all(celda in jugadas for celda in condicion):
            return condicion
    return False

def ir_click(x, y):
    global jugador_x
    global juego

    # Calcular la celda del 1 al 3 en x y y
    cell_x = int((x + tamaño // 2) // celdaT)
    cell_y = int((y + tamaño // 2) // celdaT)
    print (celdaT)
    print (cell_x)
    print (cell_y)

    #centro
    #cell por celda  
    centro_x = -tamaño // 2 + cell_x * celdaT + celdaT // 2
    centro_y = -tamaño // 2 + cell_y * celdaT + celdaT // 2

    #verificar que no este ocupada
    if evitar_iguales(cell_x, cell_y):
        return
    
    t.penup()
    t.goto(centro_x, centro_y)
    t.pendown()

  
    if jugador_x:
        juego.dibujar_equis(centro_x, centro_y)
        jugadas_x.append((cell_x,cell_y))
        jugadas_ambos.append((cell_x,cell_y))
        print(jugadas_x)
        ganaste=comprobar_ganador(jugadas_x)
        if ganaste:
            juego.dibujar_linea_ganadora(ganaste)
            print("gana jugador x")
            
    else:
        juego.dibujar_circulo(centro_x, centro_y)
        jugadas_o.append((cell_x,cell_y))
        jugadas_ambos.append((cell_x,cell_y))
        print(jugadas_o)
        ganaste=comprobar_ganador(jugadas_o)
        if ganaste:
            juego.dibujar_linea_ganadora(ganaste)
            print("gana jugador o")

    jugador_x = not jugador_x


juego = graficos(t)
start=juego.dibujar_tablero(tamaño)
pantalla.onclick(ir_click)
turtle.done()


