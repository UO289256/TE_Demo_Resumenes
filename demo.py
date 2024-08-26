"""
import os
import time
import logging
import streamlit as st
from llama_index.readers.file import PDFReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document, ServiceContext, VectorStoreIndex, Settings
from llama_index.core import SimpleDirectoryReader, get_response_synthesizer
from llama_index.core import DocumentSummaryIndex
from llama_index.core import SummaryIndex
from transformers import AutoTokenizer, pipeline
import data
import resumenes
import citas

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Directorio de los BOEs
path = './data/BOEs/'

# Configuración de la interfaz de Streamlit
st.set_page_config(page_title='Resumen de Documentos BOE', layout='wide')
st.title('Resumen de Documentos BOE')

# Información sobre los enfoques
with st.expander("Información sobre los enfoques", expanded=False):
    st.header('LLMs Tradicionales')
    st.write(
        "Los Modelos de Lenguaje de Gran Escala (LLMs) son sistemas avanzados entrenados con grandes cantidades de datos textuales. Esto les permite comprender y generar lenguaje natural, así como identificar patrones complejos y generar respuestas coherentes y contextualmente apropiadas.\n\n"
        "Debido a su habilidad para abordar una amplia variedad de tareas y comprender múltiples idiomas, estos modelos están revolucionando la interacción entre humanos y máquinas, proporcionando soluciones más precisas y efectivas en diversas áreas."
    )

    st.header('Enfoque RAG')
    st.write(
        "Los LLMs son sistemas avanzados entrenados con grandes volúmenes de datos textuales. Sin embargo, estos modelos no están específicamente entrenados con datos particulares de usuarios individuales.\n\n"
        "La Generación Aumentada por Recuperación (RAG) aborda esta limitación al integrar datos específicos con la información general a la que los LLMs ya tienen acceso.\n\n"
        "En el enfoque RAG, los datos se cargan y preparan para consultas mediante un proceso de 'indexación' . Las consultas de los usuarios se ejecutan sobre este índice, que filtra la información para identificar el contexto más relevante. Este contexto, junto con la consulta, se envía al LLM junto con un mensaje, permitiendo al modelo proporcionar una respuesta precisa y adecuada."
    )

# Generador de resúmenes
st.header('Generador de resúmenes')
col1, col2 = st.columns([2, 1])

with col1:
    nombres_archivos = data.obtener_nombres_archivos(path)
    selected_file = st.selectbox('Selecciona un documento BOE', nombres_archivos)

with col2:
    enfoque = st.selectbox('Selecciona el enfoque con el que quieres obtener el resumen.', ['LLM Tradicional', 'Enfoque RAG'])

st.write(
    "RECUERDA: El enfoque tradicional emplea un modelo de aprendizaje profundo para generar los resúmenes. Sin embargo, un BOE estándar a menudo supera la capacidad del modelo, lo que puede resultar en resúmenes insatisfactorios y en posibles inconsistencias."
)

if enfoque == 'LLM Tradicional':
    summary_method = 'LLM Tradicional'
else:
    summary_method = st.selectbox('Selecciona el método de resumen', ['Document Summary Index', 'Summary Index'])
    st.write(
        "Un Index es una estructura de datos organizada en nodos a partir de los cuales se obtiene el resumen del documento.\n\n"
        "A continuación, se puede optar entre dos métodos distintos para estructurar los datos, lo que resultará en diferentes tipos de resúmenes de los BOEs."
    )

# Botón para generar el resumen con un spinner de carga
if st.button('Generar Resumen'):
    with st.spinner('Generando resumen...'):
        time.sleep(0.5) # Simular un proceso de carga

        # Cargar el contenido del PDF seleccionado
        file_path = os.path.join(path, selected_file + ".pdf")
        docs = data.load_pdfs(path)
        text = data.obtener_texto(docs, selected_file + ".pdf")
        
        # Generar y mostrar el resumen
        st.subheader('Resumen Generado')
        if summary_method == 'LLM Tradicional':
            resumen = resumenes.resumenes("tradicional", selected_file)
            st.write(resumen)
        
        elif summary_method == 'Document Summary Index':
            #resumen = resumenes.resumenes("documentsummaryindex", selected_file)
            resumen, citas = citas.citas("documentsummaryindex", selected_file)
                    
            # Crear dos columnas: una para el resumen y otra para las citas
            col1, col2 = st.columns(2)
            
            with col1:
                st.header("Resumen del Documento")
                st.write(resumen)
            
            with col2:
                st.header("Citas")
                st.write(citas)
            
        elif summary_method == 'Summary Index':
            #resumen = resumenes.resumenes("summaryindex", selected_file)
            resumen, citas = citas.citas("summaryindex", selected_file)
            
            # Crear dos columnas: una para el resumen y otra para las citas
            col1, col2 = st.columns(2)
            
            with col1:
                st.header("Resumen del Documento")
                st.write(resumen)
            
            with col2:
                st.header("Citas")
                st.write(citas)

        with open(file_path, "rb") as file:
            st.download_button(
                label="Descargar BOE Original",
                data=file,
                file_name=f"{selected_file}.pdf",
                mime="application/pdf"
            )
"""

import os
import time
import logging
import streamlit as st
import data
import resumenes
import citas

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Directorio de los BOEs
path = './data/BOEs/'

# Configuración de la interfaz de Streamlit
st.set_page_config(page_title='Resumen de Documentos BOE', layout='wide')
st.title('Resumen de Documentos BOE')

# Inicializar estado de la aplicación
if 'resumen_generado' not in st.session_state:
    st.session_state.resumen_generado = False

if 'selected_file' not in st.session_state:
    st.session_state.selected_file = None

def reset():
    st.session_state.resumen_generado = False
    st.session_state.selected_file = None
    st.experimental_rerun()

# Mostrar la interfaz de selección si no se ha generado un resumen
if not st.session_state.resumen_generado:
    # Información sobre los enfoques
    with st.expander("Información sobre los enfoques", expanded=False):
        st.header('LLMs Tradicionales')
        st.write(
            "Los Modelos de Lenguaje de Gran Escala (LLMs) son sistemas avanzados entrenados con grandes cantidades de datos textuales..."
        )
        st.header('Enfoque RAG')
        st.write(
            "Los LLMs son sistemas avanzados entrenados con grandes volúmenes de datos textuales. Sin embargo, estos modelos no están específicamente entrenados con datos particulares de usuarios individuales..."
        )

    # Generador de resúmenes
    st.header('Generador de resúmenes')
    col1, col2 = st.columns([2, 1])

    with col1:
        nombres_archivos = data.obtener_nombres_archivos(path)
        selected_file = st.selectbox('Selecciona un documento BOE', nombres_archivos)
        st.session_state.selected_file = selected_file

    with col2:
        enfoque = st.selectbox('Selecciona el enfoque con el que quieres obtener el resumen.', ['LLM Tradicional', 'Enfoque RAG'])

    st.write(
        "RECUERDA: El enfoque tradicional emplea un modelo de aprendizaje profundo para generar los resúmenes..."
    )

    if enfoque == 'LLM Tradicional':
        summary_method = 'LLM Tradicional'
    else:
        summary_method = st.selectbox('Selecciona el método de resumen', ['Document Summary Index', 'Summary Index'])
        st.write(
            "Un Index es una estructura de datos organizada en nodos a partir de los cuales se obtiene el resumen del documento..."
        )

    if st.button('Generar Resumen'):
        # Redireccionar a una nueva "página" que muestra el progreso del resumen
        st.session_state.show_summary = True
        st.experimental_rerun()

# Mostrar el resumen si se está en el proceso de generación
if 'show_summary' in st.session_state and st.session_state.show_summary:
    with st.spinner('Generando resumen...'):
        time.sleep(0.5)  # Simular un proceso de carga

        # Cargar el contenido del PDF seleccionado
        file_path = os.path.join(path, st.session_state.selected_file + ".pdf")
        docs = data.load_pdfs(path)
        text = data.obtener_texto(docs, st.session_state.selected_file + ".pdf")
        
        # Guardar resumen en el estado
        if summary_method == 'LLM Tradicional':
            resumen = resumenes.resumenes("tradicional", st.session_state.selected_file)
        elif summary_method == 'Document Summary Index':
            resumen, citas_result = citas.citas("documentsummaryindex", st.session_state.selected_file)
            st.session_state.citas = citas_result
        elif summary_method == 'Summary Index':
            resumen, citas_result = citas.citas("summaryindex", st.session_state.selected_file)
            st.session_state.citas = citas_result
        
        st.session_state.resumen = resumen
        st.session_state.resumen_generado = True
        st.session_state.show_summary = False
        st.experimental_rerun()

# Mostrar el resumen si ya se generó
if st.session_state.resumen_generado:
    st.header('Resumen Generado')
    st.write(st.session_state.resumen)
    if summary_method == 'Document Summary Index' or summary_method == 'Summary Index':
        if st.session_state.citas:
            st.header('Citas')
            st.write(st.session_state.citas)

    file_path = os.path.join(path, st.session_state.selected_file + ".pdf")
    with open(file_path, "rb") as file:
        st.download_button(
            label="Descargar BOE Original",
            data=file,
            file_name=f"{st.session_state.selected_file}.pdf",
            mime="application/pdf"
        )
    
    # Botón para volver atrás
    st.button('Volver atrás', on_click=reset, key='reset_button')


            