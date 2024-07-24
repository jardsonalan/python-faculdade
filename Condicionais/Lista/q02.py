idade = int(input('Informe a sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade < 65:
    print('Maior de idade')
else:
    print('Pessoa idosa')