frase = input('Ingrese la palabra para verificar si es o no un HETEROGRAMA ')


letras = {}
for palabra in frase.split():
    for letra in palabra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

flag = True
for valor in letras.values():
    if (valor > 1):
        flag = False

if (flag):
    print('Es un Heterograma')
else: 
    print('No es un Heterograma')