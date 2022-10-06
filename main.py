import pandas as pd
df = pd.read_csv("dummy-actas.csv", header = 0)

schild = "Informe"
niveu = "Posgrado"
fakultaet = "Derecho"
akteur = "Estudiantes"

def filtrar(niveau, fakultaet, akteur, schild):
    df_extract = df[df['nivel'].str.contains(niveau, na=False)
        & df['unidad'].str.contains(fakultaet)
        & df['actores'].str.contains(akteur)
        # & df['vice'].str.contains(akteur) esto viene del diccionario global de vicerrectorías
        & df['tag'].str.contains(schild)]
    return df_extract['extracto']