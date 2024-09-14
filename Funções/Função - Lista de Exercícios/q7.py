def potencia(x, n):
    potencia = (x ** n)
    resultado = print(f'{x} elevado a {n} é igual a: {potencia}')
    return resultado

valorX = float(input('Informe um número: '))
valorN = int(input(f'Informe o valor que deseja elevar o número {valorX}: '))

potencia(valorX, valorN)