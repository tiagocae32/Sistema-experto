from experta import *

class Persona(Fact):
    """Hecho que representa una persona"""
    pass

class MotorCredito(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.errores = []

    @Rule(OR(
    Persona(nombre=P(lambda n: n == '' or not n.strip())),
    Persona(apellido=P(lambda a: a == '' or not a.strip())),
    Persona(edad=P(lambda e: e is None)),
    Persona(sueldo=P(lambda s: s is None)),
    Persona(antiguedad=P(lambda a: a is None))
))
    def required_fields(self):
        self.errores.append("❌ Todos los campos son obligatorios.")
        self.halt()


    @Rule(Persona(edad=P(lambda e: e is not None and e < 18)))
    def es_menor(self):
        self.errores.append("❌ Es menor de edad.")
    
    @Rule(Persona(sueldo=P(lambda s: s is not None and s < 1000)))
    def sueldo_menor(self):
        self.errores.append("❌ No cumples con el sueldo minimo.")
    
    @Rule(Persona(antiguedad=P(lambda a: a is not None and a < 12)))
    def antiguedad_menor(self):
        self.errores.append("❌ No cumples con la antigüedad mínima.")
