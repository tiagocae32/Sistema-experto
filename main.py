import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

import streamlit as st
from utils import *
from motor import MotorCredito, Persona

class SistemaExperto():

    def set_titles(self):
        st.set_page_config(page_title="Evaluador de Créditos", layout="centered")
        st.title("Autorización crédito hipotecario")

    def get_inputs(self):
        nombre = st.text_input("Nombre")
        edad_str = st.text_input("Edad")
        antiguedad_str = st.text_input("Años de antigüedad en su trabajo")
        sueldo_str = st.text_input("Sueldo")
        tipo_trabajo = st.selectbox("Tipo de trabajo", ["En relacion de dependencia", "Monotributo", "Informal"])
        valor_propiedad_str = st.text_input('Valor Propiedad (en pesos)')
        años_devolucion_str = st.selectbox("¿En cuántos años querés devolver el préstamo?", ["20", "25", "30"])
        return nombre, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str


    def evaluar_credito(self,nombre, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str):
        campos = {
            "edad": to_int(edad_str),
            "sueldo": to_int(sueldo_str),
            "valor_propiedad": to_int(valor_propiedad_str),
            "antiguedad": to_int(antiguedad_str),
            "nombre": nombre.strip(),
            "tipo_trabajo" : tipo_trabajo
        }

        # Validacion de campos
        if any(valor in (None, '') for valor in campos.values()):
            return ["❌ Todos los campos son obligatorios."], []

        engine = MotorCredito()
        engine.reset()
        engine.declare(Persona(
            nombre=campos["nombre"],
            edad=campos["edad"],
            sueldo=campos["sueldo"],
            tipo_trabajo=campos['tipo_trabajo'],
            valor_propiedad=campos["valor_propiedad"],
            antiguedad=campos["antiguedad"],
            años_devolucion=años_devolucion_str
        ))
        engine.run()
        return engine.errores, engine.prestamo_aprobado

    def main(self):
        self.set_titles()
        nombre, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str = self.get_inputs()

        if st.button("Evaluar"):
            errores, prestamo_aprobado = self.evaluar_credito(nombre, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str)
            st.subheader("Resultado")
            if len(errores) > 0:
                for error in errores:
                    st.write(error)
            else:
                for info_credito in prestamo_aprobado:
                    st.write(info_credito)

sistema_experto = SistemaExperto()
sistema_experto.main()