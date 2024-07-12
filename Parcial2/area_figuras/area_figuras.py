class Figura:
    def __init__(self,calcular_area):
        self.calcular_area=calcular_area
    
    def calcular_area(self):
        self.calcular_area

    def getInfo(self):
           print(f"Area: {self.getCalcular_area()} hp")

class Rectangulo(Figura):
    def __init__(self, calcular_area,largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def getLargo(self):
     return self._largo

    def setLargo(self,largo):
      self._largo=largo 

    def getAncho(self):
     return self._ancho

    def setAncho(self,ancho):
      self._ancho=ancho 

    def getInfo(self):
           print(f"Area: {self.getCalcular_area()},\n Largo: {self.getLargo()} , \n Ancho:  {self.getAncho()} hp")
    

class Circulo(Figura):
    def __init__(self,calcular_area, radio):
        self._radio = radio

    def getRadio(self):
      return self._radio
    def setRadio(self,radio):
      return self._radio 
    
    def getInfo(self):
           print(f"Area: {self.getCalcular_area()},\n Radio: {self.getRadio()} ,  hp")
    


class Triangulo(Figura):
    def __init__(self, calcular_area,base, altura):
        self._base = base
        self._altura = altura
    
    def getBase(self):
     return self._base

    def setBase(self,base):
      self._base=base 

    def getAltura(self):
     return self._altura

    def setAltura(self,altura):
      self._altura=altura 

    def getInfo(self):
        print(f"Area: {self.getCalcular_area()},\n Base: {self.getBase()} , \n  Altura:  {self.getAltura()} hp")    
