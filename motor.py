

from experta import *


class Persona(Fact):
    """Hecho que representa una persona"""
    pass

class MotorCredito(KnowledgeEngine):
    errores = []

    @Rule(Persona(edad=P(lambda e: e < 18)))
    def es_menor(self):
        self.errores.append("❌ Es menor de edad.")

    @Rule(Persona(antiguedad=P(lambda e: e < 12)))
    def antiguedad_menor(self):
        self.errores.append("❌ No cumples con la antiguedad minima.")
