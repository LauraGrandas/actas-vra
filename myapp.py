import streamlit as st
import pandas as pd
import categorias
import main

# create a header

st.write(
    """

    ## Clasificación de actas del Consejo Académico de la Universidad de los Andes

    """
    )


# SELECTBOX Nivel Académico
selectbox_nivel = st.sidebar.selectbox(
    "Nivel académico",
    categorias.all_niveles,
    index= 0
)

# SELECTBOX Facultades
selectbox_facultades = st.sidebar.selectbox(
    "Facultades",
    categorias.all_facultades,
    index = 0
)

# SELECTBOX Actores
selectbox_actores = st.sidebar.selectbox(
    "Actores",
    categorias.all_actores,
    index = 0
)

# SELECTBOX Vicerrectorías
selectbox_vicerrectorias = st.sidebar.selectbox(
    "Vicerrectorías",
    categorias.all_vicerrectorias,
    index = 0
)

# RADIO Todas las etiquetas
with st.sidebar:
    etiqueta = st.radio(
        "Seleccione una etiqueta",
        categorias.all_tags, 
        index = 0
    )

df = pd.read_csv("dummy-actas2.csv", header = 0)
st.write(main.filtrar(df,selectbox_nivel,selectbox_facultades,selectbox_actores,etiqueta))

def convert_df(df):
   return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

# ejemplo = main.filtrar(df,selectbox_nivel,selectbox_facultades,selectbox_actores,etiqueta)
# listas_ejemplo = ejemplo['extracto'].tolist()
# st.write(listas_ejemplo)