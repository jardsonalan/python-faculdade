idade = int(input('Informe a sua idade: '))

if idade <= 10:
    print('Valor: R$30,00')
elif idade > 10 and idade <= 29:
    print('Valor: R$60,00')
elif idade > 29 and idade <= 45:
    print('Valor: R$120,00')
elif idade > 45 and idade <= 59:
    print('Valor: R$150,00')
elif idade > 59 and idade <= 65:
    print('Valor: R$250,00')
else:
    print('Valor: R$400,00')