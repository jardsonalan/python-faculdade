def menorNumero(num1, num2, num3):
    menorNum = 0
    if num1 <= num2 and num1 <= num3:
        menorNum = num1
    elif num2 <= num1 and num2 <= num3:
        menorNum = num2
    else:
        menorNum = num3
    
    resultado = print(f'O menor número é: {menorNum}')
    return resultado

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

menorNumero(numero1, numero2, numero3)