import streamlit as st
import numpy as np
import pandas as pd
import datetime


titanic_link = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
titanic_data = pd.read_csv(titanic_link)

# Creamos un título
st.title("Titanic app")

# Creamos sidebar
sidebar = st.sidebar

# Agregamos título y texto en sidebar
sidebar.title("Esta es mi sidebar")
sidebar.write("Puedes agregar elementos en la sidebar")

# Agregamos un calendario
hoy = datetime.date.today()
fecha_hoy = sidebar.date_input("¿Cuándo es tu cumpleaños?", hoy)
st.success("Tu cumpleaños es: %s " % fecha_hoy)

# Agregamos un calendario
st.header("Titanic dataset")

bool_dataset = sidebar.checkbox("Show dataset overview?")
if bool_dataset:
    st.dataframe(titanic_data)

# Agregamos un radio_component
st.header("Class description")
selected_class = sidebar.radio("Select class: ", titanic_data['class'].unique())

st.success("Selected class: %s " % selected_class)
st.markdown("______________")

# Agregamos un selectbox_component
selected_sex = sidebar.selectbox("Select sex: ", ["Female", "Male"])
st.success("Selected sex: %s " % selected_sex)
st.markdown("______________")

# Agregamos un expander-slider
optionals = sidebar.expander("Optional Configurations", True)
fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
st.write(fare_select)

subset_fare = titanic_data[titanic_data["fare"] >= fare_select]
st.success(f"Number of records with this fare {fare_select} = {subset_fare.shape[0]}")
st.dataframe(subset_fare)
st.markdown("______________")





