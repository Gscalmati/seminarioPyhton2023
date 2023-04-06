#####################################################################################
# Funciones para INCISO A

def promedio_todos_estudiantes(informe):
    for estudiante in informe:
        prom = promedio_estudiante(estudiante)
        print('Promedio de ' + estudiante[0] + ': ' + str(prom))
    print('\n')


def promedio_estudiante(estudiante):
    puntaje = sum(estudiante[1:])
    return puntaje/len(estudiante[1:])

#####################################################################################
# Funciones para INCISO B


def promedio_general(informe):
    sumaPromedio = 0
    cantidad_alumnos = 0

    for estudiante in informes:
        sumaPromedio += promedio_estudiante(estudiante)
        cantidad_alumnos += 1

    prom_final = sumaPromedio/cantidad_alumnos
    print('Promedio General: ' + str(prom_final) + '\n')
    return prom_final


#def promedio_general_v2(informe):
#   sumaPromedio = float(sum(map(lambda e: sum(e[1:]), informe)))
#
#    prom_final = sumaPromedio/len(informe)
#
#    print('Promedio General: ' + str(prom_final) + '\n')
#    return prom_final

#####################################################################################
# Funciones para INCISO C


def alumno_mejor_promedio(informe):
    mejorPromedio = -1
    nombreAlum = ""
    for estudiante in informe:
        prom = promedio_estudiante(estudiante)
        if (prom > mejorPromedio):
            mejorPromedio = prom
            nombreAlum = estudiante[0]
    print('Alumno con Mejor Promedio: ' +
          nombreAlum + ' con ' + str(mejorPromedio))
    return [nombreAlum, mejorPromedio]

#####################################################################################
# Funciones para INCISO D


def alumno_nota_baja(informe):
    notaMasBaja = 99
    nombreAlum = ""
    for estudiante in informe:
        for notas in estudiante[1:]:
            if (notas < notaMasBaja):
                notaMasBaja = notas
                nombreAlum = estudiante[0]
    print('Alumno con Nota Mas Baja: ' +
          nombreAlum + ' con ' + str(notaMasBaja))
    return [nombreAlum, notaMasBaja]

#####################################################################################
# Programa Principal


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

metodos = {
    1: promedio_todos_estudiantes,
    2: promedio_general,
    3: alumno_mejor_promedio,
    4: alumno_nota_baja,
    #5: promedio_general_v2
}

flag = True
while (flag):
    print('1 - Calcular Promedio de Notas de Cada Estudiante')
    print('2 - Calcular Promedio de Notas General')
    print('3 - Ver Alumno con Mejor Promedio')
    print('4 - Ver Alumno con Nota mas baja')
    print('0 - Salir')
    opc = input('Ingrese opcion ')
    if (int(opc) == 0):
        flag = False
    else:
        informes = list(zip(nombres.split(), notas_1, notas_2))
        metodos[int(opc)](informes)
