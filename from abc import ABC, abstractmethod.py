from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def describir(self):
        pass

class Sedan(Carro):
    def describir(self):
        return "Este es un sedan, es cómodo y eficiente en combustible."

class SUV(Carro):
    def describir(self):
        return "Este es un SUV, es espacioso y puede manejar terrenos difíciles."

class Deportivo(Carro):
    def describir(self):
        return "Este es un deportivo, es rápido y tiene un diseño elegante."

def mostrar_descripcion(carro):
    print(carro.describir())

# Ejemplo de uso
mi_sedan = Sedan()
mi_suv = SUV()
mi_deportivo = Deportivo()

mostrar_descripcion(mi_deportivo)      
