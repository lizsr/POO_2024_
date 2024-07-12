
class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

    def info_personal(self):
        return f"Nombre: {self.nombre}\n Edad: {self.edad}\n Teléfono: {self.tel}"

class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula,informar_carrera, info_persona):
        super().__init__(nombre, edad, tel)
        self.carrera=carrera
        self.matricula=matricula
        
    def informar_carrera(self):
        print(f"Soy {self.nombre} y estudio la carrera de {self.carrera}.")

    def info_persona(self):
        print(f"soy: {self.nombre} y mi matricula es : {self.matricula} ")

    def MetodoPublico(self):
     return self.carrera
    
    def MetodoPublico(self):
     return self.matricula  
    
     def getInfo(self):
        print(f"Nombre: {self.nombre()}")

class Docentes(Personas):
    def __init__(self, nombre, edad, tel, modalidad ,num_empleado,informar_modalidad,info_persona):
        super().__init__(nombre, edad, tel)
        self._modalidad=modalidad
        self._num_empleado=num_empleado

    def informar_modalidad(self):
        print(f"Soy:  {self.nombre} y mi modalidad es : {self.modalidad}")

    def info_persona(self):
        print(f"Soy:  {self.nombre} y soy el empleado numero: {self.num_empleado}")

       


