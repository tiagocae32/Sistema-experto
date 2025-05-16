import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

import streamlit as st
from motor import MotorCredito, Persona

st.set_page_config(page_title="Sistema Experto - Edad", layout="centered")
st.title("Autorizacion credito hipotecario")

nombre = st.text_input("Nombre")
apellido = st.text_input("Apellido")
edad = st.number_input("Edad", step=1)
sueldo = st.number_input("Sueldo", step=50000)
antiguedad = st.number_input("Antigüedad (meses)", step=1)


if st.button("Evaluar"):
    engine = MotorCredito()
    engine.reset()
    engine.declare(Persona(nombre=nombre, apellido=apellido, edad=edad, sueldo=sueldo, antiguedad=antiguedad))
    engine.run()

    st.subheader("Resultado")

    if len(engine.errores) > 0:
        for error in engine.errores:
            st.error(error)
    else:
        st.success("✅ Crédito aprobado.")