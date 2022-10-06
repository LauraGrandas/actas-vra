import pandas as pd
df = pd.read_csv("dummy-actas.csv", header = 0)

# schild = "Informe"
# niveu = "Posgrado"
# fakultaet = "Derecho"
# akteur = "Estudiantes"

def filtrar(df, niveau, fakultaet, akteur, schild):
    mask_nivel = pd.DataFrame(True,index=df.index,columns=df.columns)
    mask_facultad = pd.DataFrame(True,index=df.index,columns=df.columns)
    mask_actores = pd.DataFrame(True,index=df.index,columns=df.columns)
    mask_etiqueta = pd.DataFrame(True,index=df.index,columns=df.columns)
    if niveau != 'Any':
        mask_nivel = df['nivel'].str.contains(niveau, na=False)
    if fakultaet != 'Any':
        mask_facultad = df['facultad'].str.contains(fakultaet, na=False)
    if akteur != 'Any':
        mask_actores = df['actores'].str.contains(akteur, na=False)
    # & df['vice'].str.contains(akteur) esto viene del diccionario global de vicerrectorías
    if schild != 'Any':
        mask_etiqueta = df['tag'].str.contains(schild)

    return df[mask_nivel][mask_facultad][mask_actores][mask_etiqueta]
