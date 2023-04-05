
frase = input('Ingresar frase ')

string = input('Ingrese la palabra para buscar y contar dentro de la frase ')


listaFrase = frase.split()

recuento = 0

for palabra in listaFrase:
    if string in palabra:
    # if (palabra.lower().strip(',.') == string.lower()):
        recuento = recuento + 1

print('------------------------------')
print('Para la frase: ' + frase + '\n')
print('Palabra: ' + string + '\n')
print('Resultado: ' + str(recuento))