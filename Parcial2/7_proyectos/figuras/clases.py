
class Figuras:
    
  def __init__(self,CalcularArea):
        self.Calculararea=CalcularArea
  
    
  def getInfo(self):
           print(f"Area: {self.getCalcularArea()} hp")

class Rectangulo(Figuras):
    def __init__(self, calcularArea,largo, ancho):
        super().__init__( calcularArea,largo, ancho)
        self._largo = largo
        self._ancho = ancho

   

    def getLargo(self):
     return self._largo

    def setLargo(self,largo):
      self._largo=largo 

    def getAncho(self):
     return self._ancho

    def setAncho(self,ancho):
      self._ancho=ancho 

    def getInfo(self):
           print(f"Area: {self.getCalcularArea()},\n Largo: {self.getLargo()} , \n Ancho:  {self.getAncho()} hp")
    

class Circulo(Figuras):
    def __init__(self,CalcularArea, radio):
        super().__init__( CalcularArea,radio)
        self._radio = radio

    

    def getRadio(self):
      return self._radio
    def setRadio(self,radio):
      return self._radio 
    
    def getInfo(self):
           print(f"Area: {self.getCalcularArea()},\n Radio: {self.getRadio()} ,  hp")
    


class Triangulo(Figuras):
    def __init__(self, CalcularArea,base, altura):
        super().__init__( CalcularArea,base, altura )
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
        print(f"Area: {self.getCalcularArea()},\n Base: {self.getBase()} , \n  Altura:  {self.getAltura()} hp") 