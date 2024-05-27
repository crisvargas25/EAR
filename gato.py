
class FiguraGeometrica():

    ubicacion_x = 0
    ubicacion_y = 0
    
    def __init__(self):
        None

    def dibujaFigura(self):
        None
        
    def get_area(self):
        return 999999999.9

    def modificar_x(self, x):
        self.ubicacion_x = x
    
    def modificar_y(self, y):
        self.ubicacion_y = y
    
class Rectangulo(FiguraGeometrica):

    alto = 0.0
    base = 0.0
    
    def __init__(self,alto,base):
        self.alto = float(alto)
        self.base = float(base)

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.get_area())
        
    def get_area(self):
        return self.alto * self.base


class Circulo(FiguraGeometrica):
    None # Tarea

class Triangulo(FiguraGeometrica):
    None # Tarea

# Tarea:
# Implementar Circulo & Triangulo
# Refactor Proyecto Semanal 01
# Dibujar figura a traves del metodo dibujaFigura()

    
# Aqui empiza nuestro codigo
#import turtle

#t = turtle.turtle
#prueba = Rectangulo(2,2)
#prueba.dibujaFigura(t)


prueba = Rectangulo(2,2)

print(prueba.ubicacion_x)
print(str(prueba.get_area()))