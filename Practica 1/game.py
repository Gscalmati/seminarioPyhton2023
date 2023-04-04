from random import choice, randrange
from datetime import datetime

## Defino funcion para revisar operacion
def revisar_operacion (n_1, n_2, operador):
    if (operador == "+"):
        return n_1 + n_2
    elif (operador == "-"):
        return n_1 - n_2
    elif (operador == "*"):
        return n_1 * n_2
    else :
        ## Formateamos para facilitar la respuesta de divisiones periodicas
        return format(n_1 / n_2, '.3f')

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

## Definimos variable para contar respuestas correctas
correct = 0

for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    ## Verifico si la operacion es DIVIDIR y el denominador es 0
    if (number_2 == 0 and operator == "/"):
        number_2 += 1

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")

    ## Verificamos el resultado correcto de la operacion y comparamos
    operation = revisar_operacion(number_1, number_2, operator)
    if (float(result) == float(operation)):
        correct += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos. 
print(f"\n Tardaste {total_time.seconds} segundos.")

## Y respuesta correctas
print(f"\n Tuviste {correct} respuestas correctas.")

