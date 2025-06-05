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
        st.title("Autorización crédito hipotecario", )

    def set_inputs(self):
        col1, col2,col3 = st.columns(3)
        with col1:
             cuit_str = st.text_input("Cuit")
             edad_str = st.text_input("Edad")
             antiguedad_str = st.text_input("Años de antigüedad en su trabajo")
             sueldo_str = st.text_input("Sueldo")
        with col2:
            tipo_trabajo = st.selectbox("Tipo de trabajo", ["En relacion de dependencia", "Monotributo", "Informal"], index=0)
            valor_propiedad_str = st.text_input("Valor Propiedad (en pesos)")
            años_devolucion_str = st.selectbox(
                "Plazo del prestamo (años)",
                ["20", "30"],
                index=0
            )
            banco_elegido = st.selectbox("Seleccione un banco", ["Banco Nacion", "Banco ICBC"], index=0)
        with col3:
            cobras_sueldo_banco = st.selectbox("Cobras el sueldo en este banco?", ["Si", "No"], index=0)
        return cuit_str, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str, banco_elegido,cobras_sueldo_banco
        

    def evaluar_credito(self,cuit_str, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str, banco_elegido,cobra_sueldo):
        campos = {
            "cuit": to_int(cuit_str),
            "edad": to_int(edad_str),
            "sueldo": to_int(sueldo_str),
            "valor_propiedad": to_int(valor_propiedad_str),
            "antiguedad": to_int(antiguedad_str),
            "tipo_trabajo" : tipo_trabajo,
            "banco_elegido" : banco_elegido,
            "cobra_sueldo" : cobra_sueldo
        }

        # Validacion de campos
        if any(valor in (None, '') for valor in campos.values()):
            return ["❌ Todos los campos son obligatorios."], []

        engine = MotorCredito()
        engine.reset()
        engine.declare(Persona(
            cuit=campos["cuit"],
            edad=campos["edad"],
            sueldo=campos["sueldo"],
            tipo_trabajo=campos['tipo_trabajo'],
            valor_propiedad=campos["valor_propiedad"],
            antiguedad=campos["antiguedad"],
            años_devolucion=años_devolucion_str,
            banco_elegido=campos['banco_elegido'],
            cobra_sueldo=campos['cobra_sueldo']
        ))
        engine.run()
        return engine.errores, engine.prestamo_aprobado

    def main(self):
        self.set_titles()
        cuit_str, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str, banco_elegido,cobra_sueldo = self.set_inputs()

        if st.button("Evaluar"):
            errores, prestamo_aprobado = self.evaluar_credito(cuit_str, edad_str, antiguedad_str, sueldo_str, tipo_trabajo, valor_propiedad_str, años_devolucion_str, banco_elegido,cobra_sueldo)
            st.subheader("Resultado")
            if len(errores) > 0:
                for error in errores:
                    st.write(error)
            else:
                for info_credito in prestamo_aprobado:
                     st.write(info_credito)

sistema_experto = SistemaExperto()
sistema_experto.main()