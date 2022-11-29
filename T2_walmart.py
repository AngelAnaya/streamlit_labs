import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title('Walmart USA')
st.write('El presente dashboard tiene como objetivo mostrar una visualización sobre las ventas e ingresos de productos en Walmart USA')
st.sidebar.caption('Controles para los gráficos')

df = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')
df_states = pd.read_csv("https://raw.githubusercontent.com/jeaggo/datasets/master/States_USA.csv")

df_merge = pd.merge(df, df_states, on="State")

selected_ship = st.sidebar.radio('Modo de envío: ',df['Ship Mode'].unique())

selected_category=st.sidebar.selectbox('Selecciona la categoría del producto: ',df['Category'].unique())

optional_expander = st.sidebar.expander('Configuración opcional',True)
selected_type_conditional = optional_expander.radio('Condicional: ',["Valor máximo","Valor exacto","Valor mínimo"])

selected_discount = optional_expander.slider('Selecciona el porcentaje de descuento: ',
                                            min_value=float(df['Discount'].min()),
                                            max_value=float(df['Discount'].max()))

if selected_type_conditional == "Valor máximo":
    df_selected = df_merge[(df_merge['Discount'] <= selected_discount) & 
                        (df_merge['Ship Mode'] == selected_ship) & 
                        (df_merge['Category'] == selected_category)]
elif selected_type_conditional == "Valor exacto":
    df_selected = df_merge[(df_merge['Discount'] == selected_discount) & 
                    (df_merge['Ship Mode'] == selected_ship) & 
                    (df_merge['Category'] == selected_category)]
else:
    df_selected = df_merge[(df_merge['Discount'] >= selected_discount) & 
                        (df_merge['Ship Mode'] == selected_ship) & 
                        (df_merge['Category'] == selected_category)]

#--------------------------------------------------------------------------
#DATASET
profit_medio = df_selected.groupby(['State',"Abbreviation"])['Profit'].mean().to_dict()
df_profit_medio = pd.DataFrame([key for key in profit_medio.keys()], columns=['State',"Abbreviation"])
df_profit_medio['Ganancias medias'] = [value for value in profit_medio.values()]
df_profit_medio = df_profit_medio.sort_values(by='Ganancias medias', ascending=False)
df_profit_medio.reset_index(drop=True, inplace=True)
#--------------------------------------------------------------------------

fig = go.Figure(data=go.Choropleth(locations=df_profit_medio["Abbreviation"], 
                    z = df_profit_medio["Ganancias medias"].astype(float),
                    colorbar_title = "Ganancias medias", 
                    colorscale="Viridis",
                    locationmode="USA-states",
                    marker_line_color='white',
                    text = df_profit_medio['State']))
fig.update_layout(
    title_text = 'Ganancias por tipo de producto, modo de envío y rango de descuentos por estado',
    geo_scope='usa')

st.write(fig)
st.write(df_profit_medio)