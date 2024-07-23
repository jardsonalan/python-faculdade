idade = int(input('Informe a sua idade: '))

if idade < 16:
    print('Não eleitor')
elif idade >= 16 and idade < 18 or idade >= 65:
    print('Eleitor facultativo')
elif idade >= 18 and idade < 65:
    print('Eleitor obrigatório')