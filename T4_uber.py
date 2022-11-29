import streamlit as st
import pandas as pd

st.title("Mapa de Nueva York")
st.header("Viajes en Uber")
st.write('A continuación se muestra una visualización de los viajes realizados en la ciudad de Nueva York a cierta hora del día.')
DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
DATE_COLUMN = "Date/Time"

@st.cache(allow_output_mutation=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(10000)
df = data.copy()
df["hour"] = df["date/time"].dt.hour
st.sidebar.caption('## Control para el mapa')
hour_to_filter = st.sidebar.slider('Hora del día: ',min_value = 0, max_value = 24)
filtered_df = df[df["date/time"].dt.hour == hour_to_filter]
filtered_df = filtered_df.reset_index(drop=True)
st.map(filtered_df)
st.markdown("---------------------")
st.markdown("### Datos")
st.dataframe(filtered_df)
