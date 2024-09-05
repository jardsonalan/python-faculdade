import math

while True:
    a = float(input('Informe o valor de (a): '))

    if a == 0:
        continue
    else:
        b = float(input('Informe o valor de (b): '))
        c = float(input('Informe o valor de (c): '))

        delta = (b**2)-(4*a*c)

        xv = (-b/(2*a))

        yv = -(delta/(4*a))

        bhaskaraNegativo = (-b-math.sqrt(delta))/2*a
        bhaskaraPositivo = (-b+math.sqrt(delta))/2*a

        if a > 0:
            print('a > 0, então a concatividade é para cima')
            print(f'A função é crescente ({xv}, inf)')
            print(f'A função é decrescente (inf, {xv})')
        else:
            print('a < 0, então a concatividade é para baixo')
            print(f'A função é decrescente ({xv}, inf)')
            print(f'A função é crescente (-inf, {xv})')

        if delta > 0:
            print('delta > 0, então existe X1 e X2')
        elif delta == 0:
            print('delta = 0, então existe X1 = X2')
        else:
            print('delta < 0, então NÃO existe zero real')

        print(f'O vértice é o ponto ({xv}, {yv})')
        print(f'X1: {bhaskaraPositivo}\nX2: {bhaskaraNegativo}')
        print(f'A função é positiva no intervalo ((-inf, {bhaskaraPositivo})({bhaskaraNegativo}, inf))')

    break