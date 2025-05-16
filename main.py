import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

import streamlit as st
from motor import MotorCredito, Persona

st.set_page_config(page_title="Evaluador de Créditos", layout="centered")
st.title("Autorización crédito hipotecario")

nombre = st.text_input("Nombre")
edad_str = st.text_input("Edad")
antiguedad_str = st.text_input("Antigüedad en su trabajo (meses)")
sueldo_str = st.text_input("Sueldo")
valor_propiedad_str = st.text_input('Valor Propiedad')
años_devolucion_str = st.text_input("En cuantos años queres devolver el prestamo?")

def to_int(value):
    try:
        return int(value)
    except:
        return None

edad = to_int(edad_str)
sueldo = to_int(sueldo_str)
valor_propiedad = to_int(valor_propiedad_str)
antiguedad = to_int(antiguedad_str)
años_devolucion = to_int(años_devolucion_str)

if st.button("Evaluar"):
    engine = MotorCredito()
    engine.reset()
    engine.declare(Persona(
        nombre=nombre,
        edad=edad,
        sueldo=sueldo,
        valor_propiedad=valor_propiedad,
        antiguedad=antiguedad,
        años_devolucion = años_devolucion
    ))
    engine.run()

    st.subheader("Resultado")
    if engine.errores:
        for e in engine.errores:
            st.write(e)
    else:
        st.write("✅ Crédito aprobado.")
