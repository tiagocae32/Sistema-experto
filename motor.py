from experta import *

class Persona(Fact):
    """Hecho que representa una persona"""
    pass

class MotorCredito(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.errores = []

    @Rule(OR(
        Persona(nombre=P(lambda n: not n.strip())),
        Persona(apellido=P(lambda a: not a.strip())),
    ))
    def required_fields(self):
        self.errores.append("❌ Todos los campos son obligatorios.")
        self.halt()

    @Rule(Persona(edad=P(lambda e: e < 18)))
    def es_menor(self):
        self.errores.append("❌ Es menor de edad.")
    
    @Rule(Persona(sueldo=P(lambda s: s < 1000)))
    def sueldo_menor(self):
        self.errores.append("❌ No cumples con el sueldo minimo.")
    
    @Rule(Persona(antiguedad=P(lambda a: a < 12)))
    def antiguedad_menor(self):
        self.errores.append("❌ No cumples con la antigüedad mínima.")
