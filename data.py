import os
import re
import streamlit as st
import pandas as pd
import requests
from langchain.text_splitter import CharacterTextSplitter
from llama_index.readers.file import PDFReader
from llama_index.core import SimpleDirectoryReader
from langchain_community.document_loaders import PyPDFLoader
import logging
import PyPDF2
from PyPDF2 import PdfReader

logging.basicConfig(level=logging.INFO)

FOLDER_PATH = "documents"


@st.cache_data  # for not loading the data every time the page is refreshed
def load_data():
    """
    Load data from csv files.

    Returns:
        df_data (pandas.DataFrame): The data from the 'Registros' sheet.
        df_tesauro (pandas.DataFrame): The data from the 'Tesauro' sheet.
    """
    logging.info("Loading data...")

    # Sheet with norms
    # df_data = pd.read_excel("./data/data.csv")
    df_data = pd.read_excel(
        "./data/data.xlsx", engine="openpyxl"
    )  # , sheet_name="data")

    # Some rows have erroneous URLs
    with open("./data/erroneous_urls.txt", "r") as file:
        erroneous_urls = file.readlines()

    # We will remove these rows from the data
    indexes_to_remove = []
    for url in erroneous_urls:
        url = url.strip("\n")
        # Get the indexes of the rows with the erroneous URL
        indexes = df_data[df_data["URL"] == url].index.to_list()
        indexes_to_remove.extend(indexes)

    # Once we have all the indexes, we remove the rows
    df_data = df_data.drop(indexes_to_remove)

    # Sheet with tesauro
    df_tesauro = pd.read_excel(
        "./data/Datos_DL_2022_Final.xlsm", engine="openpyxl", sheet_name="Tesauro"
    )

    logging.info("Data loaded.")

    return df_data, df_tesauro


def download_pdfs(names, urls, ids):
    """
    Download PDF files from the given URLs and save them with corresponding names.

    Args:
        names (list): List of names to use for renaming downloaded files.
        urls (list): List of URLs of the PDF files to download.

    Returns:
        pdf_names (List): List of tuples with names and IDs of the downloaded PDF files.
    """

    logging.info("Downloading PDFs...")

    urls = rename_files(urls)

    pdf_names = []
    # Iterate over names and urls simultaneously
    for name, url, id in zip(names, urls, ids):
        mod_name = name.replace(" ", "_")
        mod_name = mod_name.replace("/", "-")

        # Check if PDF file already exists
        if os.path.exists(os.path.join(FOLDER_PATH, f"{mod_name}.pdf")):
            logging.info(f"PDF for '{name}' already exists")
            pdf_names.append((name, id))
            continue
        # Send request to download PDF file
        else:
            logging.info(f"Downloading PDF for '{name}' from URL: {url}")
            try:
                response = requests.get(url)

                # Check if request was successful
                if response.status_code == 200:
                    # Save the downloaded PDF with corresponding name in the specified folder path
                    with open(
                        os.path.join(FOLDER_PATH, f"{mod_name}.pdf"), "wb"
                    ) as file:
                        file.write(response.content)
                    logging.info(
                        f"Downloaded PDF for '{name}' from URL: {url} and saved as '{os.path.join(FOLDER_PATH, f'{mod_name}.pdf')}'"
                    )
                    pdf_names.append((name, id))
                else:
                    logging.error(
                        "Error downloading the contents of ",
                        name,
                        ". Try again later.",
                    )
            except Exception as e:
                logging.error(
                    "Error downloading the contents of ", name, ". Traceback: ", e
                )

    return pdf_names

def load_pdfs(directory_path):
    """
    Carga documentos PDF desde un directorio dado.

    Args:
    - directory_path (str): Ruta al directorio que contiene los archivos PDF.

    Returns:
    - list: Lista de objetos Document cargados desde los archivos PDF.
    """
    
    # Configuración del pdf reader
    parser = PDFReader()
    file_extractor = {".pdf": parser}

    # Cargamos los documentos
    documents = SimpleDirectoryReader(directory_path, file_extractor=file_extractor).load_data()
    
    for doc in documents:
        file_name = doc.metadata['file_name']
        page_label = doc.metadata['page_label']
        #doc.id_ = page_label + "_" + file_name  # Añadir el _id como el nombre del archivo
        doc.id_ = file_name
    return documents

# Función para cargar un pdf concreto
def cargar_pdf(path):
    with open(path, 'rb') as file:
        lector_pdf = PyPDF2.PdfReader(file)
        numero_paginas = len(lector_pdf.pages)
        contenido = ""
        for i in range(numero_paginas):
            pagina = lector_pdf.pages[i]
            contenido += pagina.extract_text()
    return contenido

def rename_files(urls):
    """
    Renames the files in the given list of URLs based on specific conditions.

    Args:
        urls (list): A list of URLs.

    Returns:
        list: The modified list of URLs with renamed files.
    """
    for i in range(len(urls)):
        # for those urls that start with "https://eur-lex.europa" we need to change the substring "/EN/TXT" for "/ES/TXT/PDF"
        if urls[i].startswith("https://eur-lex.europa"):
            urls[i] = urls[i].replace("/EN/TXT", "/ES/TXT/PDF")

        # for those urls that start with "https://www.boe.es" and do not end in "pdf" we need to change the substring "act.php?id=" for pdf/2021/
        # and add "-consolidado.pdf" at the end
        if (
            urls[i].startswith("https://www.boe.es")
            and not urls[i].endswith("pdf")
            and not "codigo" in urls[i]
        ):
            # get the year from the url
            year = urls[i].split("-")[-2]
            urls[i] = (
                urls[i].replace("act.php?id=", "pdf/" + year + "/") + "-consolidado.pdf"
            )

        # for those urls that contain "codigo" replace the substring "codigo.php?id=" by "abrir_pdf.php?fich="
        # and replace everything that comes after a "&" by ".pdf"
        if "codigo.php?id=" in urls[i] and not "nota" in urls[i]:
            urls[i] = urls[i].replace("codigo.php?id=", "abrir_pdf.php?fich=")
            urls[i] = urls[i].split("&")[0] + ".pdf"

    return urls

def obtener_texto(documents, file_name):
    text = ""
    for doc in documents:
        #if doc.metadata['file_name'] == file_name and doc.metadata['page_label'] == '1':
        if doc.metadata['file_name'] == file_name:
            text += doc.text + " "
    return text
    
def clean_text(text):
    pattern = r"[^\n0-9a-zA-Z,. áéíóúÁÉÍÓÚ]"  # Matches any character that is not a number, comma, or space
    cleaned_text = re.sub(pattern, "", text)
    # replace \n with space
    cleaned_text = cleaned_text.replace("\n", " ")
    return cleaned_text

# Función para obtener nombre archivo BOEs
def obtener_nombres_archivos(directorio):
    archivos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".pdf"):
            nombre_sin_extension = os.path.splitext(archivo)[0]
            archivos.append(nombre_sin_extension)
    return archivos

    

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
