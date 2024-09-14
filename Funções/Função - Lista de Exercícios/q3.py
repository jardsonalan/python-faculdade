def maiorNumero(num1, num2, num3):
    maiorNum = 0
    if num1 >= num2 and num1 >= num3:
        maiorNum = num1
    elif num2 >= num1 and num2 >= num3:
        maiorNum = num2
    else:
        maiorNum = num3
    
    resultado = print(f'O maior número é: {maiorNum}')
    return resultado

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

maiorNumero(numero1, numero2, numero3)