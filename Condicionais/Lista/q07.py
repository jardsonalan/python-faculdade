a = float(input('Informe o valor A: '))
b = float(input('Informe o valor B: '))
c = float(input('Informe o valor C: '))

moduloA = abs(b - c)
moduloB = abs(a - c)
moduloC = abs(a - b)

if moduloA < a < b + c or moduloB < b < a + c or moduloC < c < a + b:
    print('Forma um triângulo')
else:
    print('Não formar um triângulo')