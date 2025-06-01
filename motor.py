from experta import *

class Persona(Fact):
    """Hecho que representa una persona"""
    pass

class MotorCredito(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.errores = []
        self.prestamo_aprobado = []


    @Rule(Persona(edad=P(lambda e: e is not None and (e < 18 or e > 80))))
    def es_menor(self):
        self.errores.append("❌ No cumples con el requisito de la edad.")
    
    @Rule(Persona(sueldo=P(lambda s: s is not None and s < 1000)))
    def sueldo_menor(self):
        self.errores.append("❌ No cumples con el sueldo minimo.")
    
    @Rule(Persona(antiguedad=P(lambda a: a is not None and a < 12)))
    def antiguedad_menor(self):
        self.errores.append("❌ No cumples con la antigüedad mínima.")
        
    @Rule(AND(
        Persona(edad=P(lambda e: e > 18)),
        Persona(antiguedad=P(lambda a: a > 12)),
        Persona(sueldo=MATCH.sueldo),
        Persona(valor_propiedad=MATCH.valor_propiedad),
        Persona(años_devolucion=MATCH.años_devolucion)
    ))
    def prestamo_aprobado(self, sueldo, valor_propiedad, años_devolucion):
        monto = valor_propiedad
        tasa_mensual = (6 / 100) / 12
        cantidad_cuotas = int(años_devolucion) * 12
        cuota = (monto * tasa_mensual * (1 + tasa_mensual) ** cantidad_cuotas) / ((1 + tasa_mensual) ** cantidad_cuotas - 1)
        maximo_permitido = sueldo * 0.25

        if cuota <= maximo_permitido:
           self.prestamo_aprobado.append("✅ Préstamo Aprobado")
           self.prestamo_aprobado.append(f"🧾 Cantidad de cuotas: {cantidad_cuotas}")
           self.prestamo_aprobado.append(f"💰 Cuota mensual estimada: ${round(cuota, 2)}")
        else:
            self.errores.append(f"❌ Has superado el maximo permitido por cuota")