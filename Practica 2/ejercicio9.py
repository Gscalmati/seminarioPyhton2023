palabra = input('Ingrese palabra para ser calculada ')

palabra = palabra.strip()

puntajes = {
    'A, E, I, O, U, L, N, R, S, T' :1,
    'D, G' :2,
    'B, C, M, P' :3,
    'F, H, V, W, Y' :4,
    'K' :5,
    'J, X' :8,
     'Q, Z' :10
}

puntaje = 0
for letra in palabra:
    for letras_tabla, valor in puntajes.items():
       if letra.upper() in letras_tabla:
           puntaje += valor

print(palabra + ' - Pts: ' + str(puntaje))