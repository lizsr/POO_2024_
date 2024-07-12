



from clases import *





def calcular_area_rectangulo(self):
    return self._largo * self._ancho
Rectangulo = Rectangulo(largo=5, ancho=7)
Rectangulo.calcular_area = calcular_area_rectangulo
Rectangulo.getInfo()


circulo = Circulo(pi=3.1416, radio=2)
def calcular_area_circulo(self):
    import math
    return math.pi * self._radio ** 2

circulo.calcular_area = calcular_area_circulo
circulo.getInfo()


triangulo = Triangulo(base=8, altura=10)
def calcular_area_triangulo(self):
    return 0.5 * self._base * self._altura

triangulo.calcular_area = calcular_area_triangulo
triangulo.getInfo()

