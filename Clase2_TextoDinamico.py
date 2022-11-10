import streamlit as st

def bienvenida(nombre):
    mymessage = "Bienvenido(a):" + nombre
    return mymessage

myname = st.text_input("Nombre: ")
if (myname):
    mensaje = bienvenida(myname)
    st.write(f"Mensaje: {myname}")