import streamlit as st
import time
import numpy as np
import pandas as pd
import calendar
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Netflix Filters",
                page_icon=":movie_camera:",
                layout="wide")

st.title('Netflix Filters :movie_camera:')

DATA_UPLOAD='movies.csv'
df=pd.read_csv(DATA_UPLOAD)


mytitle=st.sidebar.text_input('Type the title of the movie')

if st.sidebar.button('Search'):
#    df_title = df.loc[(df['name'] == mytitle), ['company','director','genre','name']]
    filtered_data_filme = df[df['name'].str.upper().str.contains(mytitle.upper())]
#    df_title = df['name'].str.upper().str.contains(mytitle.upper())
    count_row=filtered_data_filme.shape[0]
    st.write(f'Total movies: {count_row}')
    st.dataframe(filtered_data_filme)

director_list=df['director'].unique().tolist()
mydirector=st.sidebar.selectbox('Select the director: ', director_list)
showall=st.sidebar.checkbox('Show all?')

@st.cache
def load_data(select_director):
    data=pd.read_csv(DATA_UPLOAD)
    filtered_dir=data[data['director'].str.contains(select_director)]
    return filtered_dir

if (mydirector):
    fitleredbydir=load_data(mydirector)
    count_row=fitleredbydir.shape[0]
    st.write(f'Total names: {count_row}')
    st.dataframe(fitleredbydir)  

if (showall):
    st.dataframe(df)