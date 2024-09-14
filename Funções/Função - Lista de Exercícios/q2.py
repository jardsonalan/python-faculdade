def menorNumero(num1, num2):
    menorNum = 0
    if num1 < num2:
        menorNum = num1
    else:
        menorNum = num2
    
    resultado = print(f'O menor número é: {menorNum}')
    return resultado

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

menorNumero(numero1, numero2)