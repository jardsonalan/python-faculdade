def maiorNumero(num1, num2):
    maiorNum = 0
    if num1 > num2:
        maiorNum = num1
    else:
        maiorNum = num2
    
    resultado = print(f'O maior número é: {maiorNum}')
    return resultado

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

maiorNumero(numero1, numero2)