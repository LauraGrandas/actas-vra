# actas-vra
Clasificación por etiquetas de las actas del Consejo Académico de la Universidad de los Andes.

### Descripción: 
Cada documento de la carpeta actas contiene el acta correspondiente a un día de sesión del Consejo Académico de la Universidad de los Andes. Vamos a tomar unas etiquetas predeterminadas para extraer extractos de interés de estos documentos. Dos extractos idénticos pueden tener la misma etiqueta. 

### Contenidos de este repositorio:
1. categorias.py creates the necessary dictionaries to filter the documents
2. main.py makes the selection of extracts using the inputs from categories
3. myapp.py is the streamlit app

To run this repo locally in linux/mac use the following two lines on a terminal within the folder containing this repo: 

chmod +x app-install.sh
./app-install.sh

If you are working from within the repository on your local machine, run the app using the following command from the local folder.

streamlit run myapp.py
