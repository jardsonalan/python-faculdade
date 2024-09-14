def exibeOpcoes():
    print('-'*20+'Menu'+'-'*20)
    print('0 - Sair')
    print('1 - Maior número entre 2 números')
    print('2 - Menor número entre 2 números')
    print('3 - Maior número entre 3 números')
    print('4 - Menor número entre 3 números')
    opcao = int(input('\nInforme a opção: '))
    return opcao

def maiorNumeroDois(num1, num2):
    maiorNum = 0
    if num1 > num2:
        maiorNum = num1
    else:
        maiorNum = num2
    
    resultado = print(f'O maior número é: {maiorNum}')
    return resultado

def menorNumeroDois(num1, num2):
    menorNum = 0
    if num1 < num2:
        menorNum = num1
    else:
        menorNum = num2
    
    resultado = print(f'O menor número é: {menorNum}')
    return resultado

def maiorNumeroTres(num1, num2, num3):
    maiorNum = 0
    if num1 >= num2 and num1 >= num3:
        maiorNum = num1
    elif num2 >= num1 and num2 >= num3:
        maiorNum = num2
    else:
        maiorNum = num3
    
    resultado = print(f'O maior número é: {maiorNum}')
    return resultado

def menorNumeroTres(num1, num2, num3):
    menorNum = 0
    if num1 <= num2 and num1 <= num3:
        menorNum = num1
    elif num2 <= num1 and num2 <= num3:
        menorNum = num2
    else:
        menorNum = num3
    
    resultado = print(f'O menor número é: {menorNum}')
    return resultado

def main():
    opcao = 1
    while opcao != 0:
        opcao = exibeOpcoes()

        if opcao <= 0:
            break
        
        elif opcao == 1:
            numero1 = int(input('Informe o primeiro número: '))
            numero2 = int(input('Informe o segundo número: '))

            maiorNumeroDois(numero1, numero2)
        
        elif opcao == 2:
            numero1 = int(input('Informe o primeiro número: '))
            numero2 = int(input('Informe o segundo número: '))

            menorNumeroDois(numero1, numero2)

        elif opcao == 3:
            numero1 = int(input('Informe o primeiro número: '))
            numero2 = int(input('Informe o segundo número: '))
            numero3 = int(input('Informe o terceiro número: '))

            maiorNumeroTres(numero1, numero2, numero3)

        elif opcao == 4:
            numero1 = int(input('Informe o primeiro número: '))
            numero2 = int(input('Informe o segundo número: '))
            numero3 = int(input('Informe o terceiro número: '))

            menorNumeroTres(numero1, numero2, numero3)

main()