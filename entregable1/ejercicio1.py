import csv
import os

def accesoUsuario (archivo, orden='None'):
    csvreaderDict = csv.DictReader(archivo, delimiter=',')
    usuarios = {}

    # Recorro archivo CSV verificando la existencia del campo en el dict USUARIOS, si existe, incremento, sino, creo campo nuevo
    for linea in csvreaderDict:
        nombreUsuario = linea['Nombre completo del usuario']
        if nombreUsuario in usuarios:
            usuarios[nombreUsuario] += 1
        else:
            usuarios[nombreUsuario] = 1

    # Ordeno en base al parámetro opcional "orden"
    if (orden == 'A'):
        usuarios = sorted(usuarios.items(), key=lambda item: item[1], reverse=True)
    elif (orden == 'D'):
        usuarios = sorted(usuarios.items(), key=lambda item: item[1], reverse=False)

    # Devuelvo los 5 primeros items
    return tuple(usuarios.items())[0:5]

# Defino rutas y abro el archivo
ruta = os.path.dirname(os.path.realpath('.'))
ruta_archivo = os.path.join(ruta, 'entregable1', 'log_catedras.csv')
archivo_poke = open(ruta_archivo, 'r')

# Invoco funcion
usuarios = accesoUsuario(archivo_poke, 'None')

# Imprimo información
print('--------------------------------------------')
print('Usuarios en el sistema - Cantidad de Accesos')
print('--------------------------------------------')
for usuario in usuarios:
    print(f'{usuario[0]:22} - {usuario[1]:10}')

# Cierro el archivo
archivo_poke.close()