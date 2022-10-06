import pandas as pd
df = pd.read_csv("dummy-actas.csv", header = 0)

palabra = "Informe"
df_extract = df[df['tag'].str.contains("Informe")]
objeto = df_extract['extracto']