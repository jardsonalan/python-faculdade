number1 = float(input('Informe um número: '))
number2 = float(input('Informe outro número: '))

print('-'*40)
print('Qual operação abaixo você deseja: ')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
print('-'*40)

controler = int(input('Informe a opção desejada: '))

if controler == 1:
    operador = number1 + number2
    print('Operação: Soma')
    print('Resultado: %.2f' %operador)
elif controler == 2:
    operador = number1 - number2
    print('Operação: Subtração')
    print('Resultado: %.2f' %operador)
elif controler == 3:
    operador = number1 * number2
    print('Operação: Multiplicação')
    print('Resultado: %.2f' %operador)
elif controler == 4:
    operador = number1 / number2
    print('Operação: Divisão')
    print('Resultado: %.2f' %operador)
else:
    print('Opção não disponível!')