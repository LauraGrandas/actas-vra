import streamlit as st
import pandas as pd
import categorias

# create a header

st.write(
    """

    ## Clasificación de actas del Consejo Académico de la Universidad de los Andes

    """
    )


# SELECTBOX Nivel Académico
add_selectbox = st.sidebar.selectbox(
    "Nivel académico",
    categorias.all_niveles,
    index= 0
)

# SELECTBOX Facultades
add_selectbox = st.sidebar.selectbox(
    "Facultades",
    categorias.all_facultades,
    index = 0
)

# SELECTBOX Actores
add_selectbox = st.sidebar.selectbox(
    "Actores",
    categorias.all_actores,
    index = 0
)

# SELECTBOX Vicerrectorías
add_selectbox = st.sidebar.selectbox(
    "Vicerrectorías",
    categorias.all_vicerrectorias,
    index = 0
)

# RADIO Todas las etiquetas
with st.sidebar:
    add_radio = st.radio(
        "Seleccione una etiqueta",
        categorias.all_tags
    )

#ya fuera del sidebar
df = pd.read_csv("dummy-actas.csv", header = 0)

palabra = "Informe"
df_extract = df[df['tag'].str.contains("Informe")]
objeto = df_extract['extracto']#.to_list()
st.write(objeto)