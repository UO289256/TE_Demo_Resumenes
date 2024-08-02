# TE_Demo_Resumenes
Demo de una aplicación que obtiene resumenes de Boletines Oficiales del Estado (BOEs) 

La manera más rápida de instalar el software es hacerlo mediante un entorno virtual en python con conda:

```
conda create -n cities-datalex python=3.10
conda activate cities-datalex
pip install -r requirements.txt
```

Otra opción es utilizar un studio de lightning.ai. Dentro del studio clonar el repositorio (View - Command Palette - Git:Clone) y en una terminal hacer el pip install - r requirements.txt. Cada studio corresponde a un entorno virtual diferente por lo que no es necesario crear ningún entorno.

Una vez instalados los paquetes necesarios para ejecutar la interfaz gráfica:

```
streamlit run demo.py
```

Para ejecutar con ollama y llama3:

```
curl -fsSL https://ollama.com/install.sh | sh

ollama pull llama3
```
