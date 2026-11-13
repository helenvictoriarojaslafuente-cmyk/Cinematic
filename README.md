#Guía de Instalación y Ejecución

Este documento explica los pasos necesarios para configurar el entorno y ejecutar la interfaz visual del proyecto utilizando **Streamlit** desde **Visual Studio Code**.

---
Pasos para iniciar la interfaz visual

1. Abre la terminal en Visual Studio Code
Abre el proyecto en VS Code y despliega la terminal integrada presionando el atajo:
> **`Ctrl` + `Shift` + `ñ`** *(o desde el menú superior: `Terminal` > `Nueva terminal`)*.

 2. Instala las dependencias necesarias
En la terminal, ejecuta el siguiente comando para instalar **Streamlit** (el entorno visual) y **Pillow** (para el manejo de imágenes):

py -m pip install streamlit pillow

 3. Inicia la aplicación
Asegúrate de que tu terminal esté ubicada en la carpeta raíz del proyecto (donde se encuentra el archivo `app.py`) y ejecuta:

py -m streamlit run app.py

4. Configuración inicial de Streamlit
La primera vez que ejecutes Streamlit, la terminal te pedirá ingresar un correo electrónico para recibir avisos y novedades. **No es necesario escribir nada**, simplemente presiona la tecla **`ENTER`** para omitir este paso.

5. ¡Listo, Disfruta!
Automáticamente se abrirá una pestaña en tu navegador web predeterminado mostrando la interfaz visual del proyecto.
