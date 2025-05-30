from experta import *

class Persona(Fact):
    """Hecho que representa una persona"""
    pass

class MotorCredito(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.errores = []
        self.prestamo_aprobado = []


    @Rule(Persona(edad=P(lambda e: e is not None and e < 18)))
    def es_menor(self):
        self.errores.append("❌ Es menor de edad.")
    
    @Rule(Persona(sueldo=P(lambda s: s is not None and s < 1000)))
    def sueldo_menor(self):
        self.errores.append("❌ No cumples con el sueldo minimo.")
    
    @Rule(Persona(antiguedad=P(lambda a: a is not None and a < 12)))
    def antiguedad_menor(self):
        self.errores.append("❌ No cumples con la antigüedad mínima.")

    @Rule(AND(
        Persona(edad=P(lambda e: e > 18)),
        Persona(sueldo=P(lambda s: s > 1000)),
        Persona(antiguedad=P(lambda a: a > 12))
    ))
    def prestamo_aprobado(self):
        self.prestamo_aprobado.append("✅ Prestamo Aprobado")
