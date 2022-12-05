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

DATA_UPLOAD='citibike-tripdata.csv'
df=pd.read_csv(DATA_UPLOAD)