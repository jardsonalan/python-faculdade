quantKwh = float(input('Informe a quantidade de KWh consumida: '))

print('-'*40)
print('Tipos de instalação:')
print('R - Residências\nI - Indústrias\nC - Comércios')
print('-'*40)

tipoInstalação = input('Informe o tipo de instalação: ').upper()

if tipoInstalação == 'R':
    if quantKwh <= 500:
        operador = quantKwh * 0.40
        print('Total a pagar: R$%.2f' %operador)
    else:
        operador = quantKwh * 0.65
        print('Total a pagar: R$%.2f' %operador)
    
elif tipoInstalação == 'C':
    if quantKwh <= 1000:
        operador = quantKwh * 0.55
        print('Total a pagar: R$%.2f' %operador)
    else:
        operador = quantKwh * 0.60
        print('Total a pagar: R$%.2f' %operador)

elif tipoInstalação == 'I':
    if quantKwh <= 5000:
        operador = quantKwh * 0.55
        print('Total a pagar: R$%.2f' %operador)
    else:
        operador = quantKwh * 0.60
        print('Total a pagar: R$%.2f' %operador)