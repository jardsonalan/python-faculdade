idade = int(input('Informe a sua idade: '))

if idade <= 15:
    print('Os calculos para essa idade são inválidos!')
else:
    print('-'*40)

    altura = float(input('Informe sua altura (m): '))
    peso = float(input('Informe o seu peso (kg): '))

    print('-'*40)

    calculo = (peso / (altura**2))
    if calculo < 17:
        print('Muito abaixo do peso')
    elif calculo >= 17 and calculo <= 18.49:
        print('Abaixo do peso')
    elif calculo >= 18.5 and calculo <= 24.99:
        print('Peso normal')
    elif calculo >= 25 and calculo <= 29.99:
        print('Acima do peso')
    elif calculo >= 30 and calculo <= 34.99:
        print('Obesidade I')
    elif calculo >= 35 and calculo <= 39.99:
        print('Obesidade II (severa)')
    elif calculo > 40:
        print('Obesidade III (mórbida)')