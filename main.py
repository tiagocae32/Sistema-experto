import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

import streamlit as st
from motor import MotorCredito, Persona

st.set_page_config(page_title="Sistema Experto - Edad", layout="centered")
st.title("Autorizacion credito hipotecario")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value=0, max_value=120)
sueldo = st.number_input("sueldo", min_value=0)
antiguedad = st.number_input("antiguedad(meses)", min_value=0)

if st.button("Evaluar"):
    engine = MotorCredito()
    engine.reset()
    engine.declare(Persona(nombre=nombre, edad=edad, sueldo=sueldo, antiguedad=antiguedad))
    engine.run()

    st.subheader("Resultado")

    if len(engine.errores) > 0:
        for error in engine.errores:
            st.error(error)
    else:
        st.success("✅ Crédito aprobado.")