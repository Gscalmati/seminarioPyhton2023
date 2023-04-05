
import string

texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

listaTexto = texto.split()

informe = {
    "minus": 0,
    "mayus": 0,
    "especiales": 0,
    "palabras": 0
}

for palabra in listaTexto:
    informe["palabras"] += 1
    for letras in palabra:
        if letras in string.ascii_letters:
            if letras in string.ascii_uppercase:
                informe["mayus"] += 1
            else:
                informe["minus"] += 1
        else:
            informe["especiales"] +=1

print(informe)