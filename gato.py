import turtle
import datetime

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.color("white")
pantalla = turtle.Screen()
t.speed(0)
t.color("red")
for i in range (1,200):
    t.forward(i+i)
    t.left(68)


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

jugadas_ambos = []
jugadas_x = []
jugadas_o = []

tamaño = 800
celdaT = tamaño // 3
jugador_x = True

class graficos:
    def __init__(self, t):
        self.t = t

    def dibujar_tablero(self, tamaño):
        t = self.t
        t.penup()
        t.goto(-tamaño // 2, tamaño // 6)
        t.pendown()
        t.forward(tamaño)

        t.penup()
        t.goto(-tamaño // 2, -tamaño // 6)
        t.pendown()
        t.forward(tamaño)

        t.right(90)

        t.penup()
        t.goto(-tamaño // 6, tamaño // 2)
        t.pendown()
        t.forward(tamaño)

        t.penup()
        t.goto(tamaño // 6, tamaño // 2)
        t.pendown()
        t.forward(tamaño)
        t.penup()
        t.home()

    def dibujar_equis(self, x, y):
        t = self.t
        equis = 160
        t.penup()
        t.goto(x - equis // 2, y + equis // 2)
        t.pendown()
        t.goto(x + equis // 2, y - equis // 2)
        t.penup()
        t.goto(x - equis // 2, y - equis // 2)
        t.pendown()
        t.goto(x + equis // 2, y + equis // 2)
        t.penup()

    def dibujar_circulo(self, x, y):
        t = self.t
        radio = 100
        t.speed(0)
        t.penup()
        t.goto(x, y - radio)
        t.pendown()
        t.circle(radio)
        t.penup()

    def dibujar_linea_ganadora(self, condicion):
        t = self.t
        x1, y1 = condicion[0]
        x2, y2 = condicion[-1]

        c_inicial_x = -tamaño // 2 + x1 * celdaT + celdaT // 2
        c_inicial_y = -tamaño // 2 + y1 * celdaT + celdaT // 2
        c_final_x = -tamaño // 2 + x2 * celdaT + celdaT // 2
        c_final_y = -tamaño // 2 + y2 * celdaT + celdaT // 2

        t.penup()
        t.color("yellow")
        t.speed(5)
        t.pensize(10)
        t.goto(c_inicial_x, c_inicial_y)
        t.pendown()
        t.goto(c_final_x, c_final_y)
        t.penup()
        t.color("white")
        t.speed(0)
        t.pensize(5)

class juego:
    def __init__(self, t, graficos):
        self.t = t
        self.graficos = graficos
        self.nombre_archivo = self.generar_nombre_archivo()

    def evitar_iguales(self, cell_x, cell_y):
        return (cell_x, cell_y) in jugadas_ambos

    def comprobar_ganador(self, jugadas):
        for condicion in condiciones_ganadoras:
            if all(celda in jugadas for celda in condicion):
                return condicion
        return False

    def ir_click(self, x, y):
        global jugador_x
        celdaT = tamaño // 3

        cell_x = int((x + tamaño // 2) // celdaT)
        cell_y = int((y + tamaño // 2) // celdaT)
        print(celdaT)
        print(cell_x)
        print(cell_y)

        centro_x = -tamaño // 2 + cell_x * celdaT + celdaT // 2
        centro_y = -tamaño // 2 + cell_y * celdaT + celdaT // 2

        if self.evitar_iguales(cell_x, cell_y):
            return
        
        t.penup()
        t.goto(centro_x, centro_y)
        t.pendown()

        if jugador_x:
            self.graficos.dibujar_equis(centro_x, centro_y)
            jugadas_x.append((cell_x, cell_y))
            jugadas_ambos.append((cell_x, cell_y))
            print(jugadas_x)
            ganaste = self.comprobar_ganador(jugadas_x)
            if ganaste:
                self.graficos.dibujar_linea_ganadora(ganaste)
                print("Gana jugador X")
                pantalla.onclick(None)

        else:
            self.graficos.dibujar_circulo(centro_x, centro_y)
            jugadas_o.append((cell_x, cell_y))
            jugadas_ambos.append((cell_x, cell_y))
            print(jugadas_o)
            ganaste = self.comprobar_ganador(jugadas_o)
            if ganaste:
                self.graficos.dibujar_linea_ganadora(ganaste)
                print("Gana jugador O")
                pantalla.onclick(None)

        jugador_x = not jugador_x
        lista_traducida = self.traducir(jugadas_x, jugadas_o)
        print(lista_traducida)

    def posicion_1_a_9(self, jugada):
        mapeo = {
            (0, 0): 7,
            (0, 1): 4,
            (0, 2): 1,
            (1, 0): 8,
            (1, 1): 5,
            (1, 2): 2,
            (2, 0): 9,
            (2, 1): 6,
            (2, 2): 3
        }
        return mapeo.get(jugada)

    def traducir(self, jugadas_x, jugadas_o):
        lista = [" " for _ in range(9)]
        
        for jugada in jugadas_x:
            indice = self.posicion_1_a_9(jugada)
            lista[indice - 1] = "x"

        for jugada in jugadas_o:
            indice = self.posicion_1_a_9(jugada)
            lista[indice - 1] = "o"

        self.escribir_movimientos_txt(lista)
        return lista

    def escribir_movimientos_txt(self, lista):
        with open(self.nombre_archivo, mode='a', newline='') as archivo_txt:
            archivo_txt.write(''.join(lista) + '\n')

    def generar_nombre_archivo(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        return f"movimientos_{timestamp}.txt"
    
graficos_instancia = graficos(t)
juego_instancia = juego(t, graficos_instancia)
graficos_instancia.dibujar_tablero(tamaño)
pantalla.onclick(juego_instancia.ir_click)
turtle.done()
