def exibeMenu():
    print('#### MENU ####\n')
    print('0 - SAIR')
    print('1 - SOMAR')
    print('2 - SUBTRAIR')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def somar(numero1, numero2):
    resultado = numero1+numero2
    return resultado

def subtrair(numero1, numero2):
    resultado = numero1-numero2
    return resultado

opcao=1
num1=0
num2=0
resultado=0

while opcao != 0:
    opcao = exibeMenu()
    if opcao <= 0:
        break

    num1 = float(input('Informe o primeiro número para a operação: '))
    num2 = float(input('Informe o segundo número para a operação: '))

    if opcao == 1:
        resultado = somar(num1, num2)

    elif opcao == 2:
        resultado = subtrair(num1, num2)

    print(f'Resultado: {resultado}')