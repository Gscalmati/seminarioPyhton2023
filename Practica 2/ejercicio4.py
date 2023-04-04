
def definirCategoria(cantidad):
    if (cantidad <= 12):
        return "Fáciles de leer"
    elif (cantidad <= 17):
        return "Aceptables para leer"
    elif (cantidad <= 25):
        return "Díficiles de leer"
    elif():
        return "Muy díficiles de leer"




evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""

# Divido el texto en 2 partes, titulo y resumen
text = evaluar.split('\n')
# Asigno cada parte a una variable
titulo = text[0]
resumen = text[1:-1]

# Le quito el "titulo:"
contenido_titulo = titulo.split(':')[1]


# Le quito el "resumen:"
primer_oracion = resumen[0][9:-1] 
contenido_resumen = resumen[1:-1]
contenido_resumen.insert(0, primer_oracion)

# Creo el diccionario que va ser utilizado de informe
informe = {
    "Titulo": "ok",
    "Fáciles de leer": 0,
    "Aceptables para leer": 0,
    "Díficiles de leer": 0,
    "Muy difíciles de leer": 0
}

# Cuento las palabras del título
cant_palabras = 0
for word in contenido_titulo.split():
    cant_palabras = cant_palabras +1
if (cant_palabras >= 10):
    informe['Titulo'] = "Titulo muy largo"


# Cuento las palabras de cada oración para definir las categorías de cada oración
for phrase in contenido_resumen:
    cant_palabras = 0
    for word in phrase.split():
        cant_palabras = cant_palabras +1
    informe[definirCategoria(cant_palabras)] += 1

print(informe)