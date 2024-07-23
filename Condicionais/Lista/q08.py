a = float(input('Informe o valor A: '))
b = float(input('Informe o valor B: '))
c = float(input('Informe o valor C: '))

moduloA = abs(b - c)
moduloB = abs(a - c)
moduloC = abs(a - b)

if moduloA < a < b + c or moduloB < b < a + c or moduloC < c < a + b:
    if a != b !=c:
        print('Triângulo escaleno')
    elif a == b == c:
        print('Triângulo equilátero')
    elif a == b != c or b == c != a or a == c != b:
        print('Triângulo isósceles')
else:
    print('Não formar um triângulo')