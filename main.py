import streamlit as st
from motor import MotorCredito, Persona

st.title("Autorización crédito hipotecario")

nombre = st.text_input("Nombre")
apellido = st.text_input("Apellido")
edad_str = st.text_input("Edad")
sueldo_str = st.text_input("Sueldo")
antiguedad_str = st.text_input("Antigüedad (meses)")

def to_int(value):
    try:
        return int(value)
    except:
        return None

edad = to_int(edad_str)
sueldo = to_int(sueldo_str)
antiguedad = to_int(antiguedad_str)

if st.button("Evaluar"):
    engine = MotorCredito()
    engine.reset()
    engine.declare(Persona(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        sueldo=sueldo,
        antiguedad=antiguedad
    ))
    engine.run()

    st.subheader("Resultado")
    if engine.errores:
        for e in engine.errores:
            st.write(e)
    else:
        st.write("✅ Crédito aprobado.")
