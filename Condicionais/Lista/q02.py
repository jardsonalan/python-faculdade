idade = int(input('Informe a sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade < 65:
    print('Maior de idade')
elif idade >= 65:
    print('Pessoa idosa')