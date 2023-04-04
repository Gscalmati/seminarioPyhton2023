import string 

jupyter_info = """ JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones.
"""

letra = input('Ingrese una letra ')
flag = letra in string.ascii_letters
while (not flag):
    letra = input('Ingrese una letra valida ')       
    flag = letra in string.ascii_letters

listaDeTexto = jupyter_info.split()

for word in listaDeTexto:
    if (word.lower().split()[0].startswith(letra.lower())):
        print(word)