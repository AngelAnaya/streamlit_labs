import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title('Walmart USA')
st.write('''El presente dashboard tiene como objetivo mostrar una visualización a través de 
        gráficas de algunas de las variables del Dataset de Walmart USA. Es posible seleccionar si se 
        requiere un análisis general o uno por estado.''')
st.sidebar.caption('Controles para los gráficos')

df = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

tipo_analisis = st.sidebar.radio('Tipo de análisis: ', ["Análisis por estado","Análisis general"])
estado_seleccionado = st.sidebar.selectbox('Selecciona el estado: ',df['State'].unique())


if tipo_analisis == "Análisis por estado":
    df_selected = df[df["State"] == estado_seleccionado]
else:
    df_selected = df

#--------------------------------------------------------------------------
# GRÁFICO DE BARRA
st.markdown("### Gráfico de barras")
fig_1 = px.histogram(df_selected, x="Ship Mode", y="Profit",
             color='Category', barmode='group',
             histfunc='avg',
             height=400)

st.write(fig_1)
#--------------------------------------------------------------------------
# GRÁFICO DE PASTEL
st.markdown("### Gráfico de pastel")
val_pie = df_selected.groupby(['Category'])['Category'].count().to_dict()
df_pie = pd.DataFrame([key for key in val_pie.keys()], columns=['Category'])
df_pie['Número de productos'] = [value for value in val_pie.values()]
df_pie = df_pie.sort_values(by='Número de productos', ascending=False)
df_pie.reset_index(drop=True, inplace=True)

fig_2 = go.Figure(data=[go.Pie(labels=df_pie['Category'], values=df_pie['Número de productos'], textinfo='label+percent',
                            insidetextorientation='radial',
                             marker_colors = ['rgb(93, 109, 126)', 'rgb(247, 220, 111)', 'rgb(150, 220, 111)']
                            )])
fig_2.update_traces(hole=.4, hoverinfo="label+percent+name")
fig_2.update_layout(hoverlabel_font_family = 'Arial', hoverlabel_font_size = 15,
                  annotations=[dict(text='Categorías de productos',x=0.5, y=0.5, font_size=12, showarrow=False)],
                  margin = dict(t=30, l=120, r=180, b=30))
st.write(fig_2)
#--------------------------------------------------------------------------
# HISTOGRAMA
st.markdown("### Histograma")
fig_3 = px.histogram(df_selected, x="Profit", nbins=100)
st.write(fig_3)


