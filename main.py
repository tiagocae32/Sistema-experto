import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

import streamlit as st
from utils import *
from motor import MotorCredito, Persona


def set_titles():
    st.set_page_config(page_title="Evaluador de Créditos", layout="centered")
    st.title("Autorización crédito hipotecario")


def get_inputs():
    nombre = st.text_input("Nombre")
    edad_str = st.text_input("Edad")
    antiguedad_str = st.text_input("Antigüedad en su trabajo (meses)")
    sueldo_str = st.text_input("Sueldo")
    valor_propiedad_str = st.text_input('Valor Propiedad')
    años_devolucion_str = st.text_input("En cuantos años queres devolver el prestamo?")
    return nombre, edad_str, antiguedad_str, sueldo_str, valor_propiedad_str, años_devolucion_str


def evaluar_credito(nombre, edad_str, antiguedad_str, sueldo_str, valor_propiedad_str, años_devolucion_str):
    edad = to_int(edad_str)
    sueldo = to_int(sueldo_str)
    valor_propiedad = to_int(valor_propiedad_str)
    antiguedad = to_int(antiguedad_str)
    años_devolucion = to_int(años_devolucion_str)

    engine = MotorCredito()
    engine.reset()
    engine.declare(Persona(
        nombre=nombre,
        edad=edad,
        sueldo=sueldo,
        valor_propiedad=valor_propiedad,
        antiguedad=antiguedad,
        años_devolucion=años_devolucion
    ))
    engine.run()
    return engine.errores


def main():
    set_titles()
    nombre, edad_str, antiguedad_str, sueldo_str, valor_propiedad_str, años_devolucion_str = get_inputs()

    if st.button("Evaluar"):
        errores = evaluar_credito(nombre, edad_str, antiguedad_str, sueldo_str, valor_propiedad_str, años_devolucion_str)

        st.subheader("Resultado")
        if errores:
            for e in errores:
                st.write(e)
        else:
            st.write("✅ Crédito aprobado.")


if __name__ == "__main__":
    main()
