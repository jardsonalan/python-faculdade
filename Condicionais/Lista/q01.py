saldoMedio = float(input('Informe o saldo médio: '))

if saldoMedio <= 500:
    print('Nenhum crédito')
elif saldoMedio <= 1000:
    valorCredito = (saldoMedio*(30/100))
    print('Saldo médio: R$%.2f\nValor de crédito: R$%.2f' %(saldoMedio, valorCredito))
elif saldoMedio <= 3000:
    valorCredito = (saldoMedio*(40/100))
    print('Saldo médio: R$%.2f\nValor de crédito: R$%.2f' %(saldoMedio, valorCredito))
else:
    valorCredito = (saldoMedio*(50/100))
    print('Saldo médio: R$%.2f\nValor de crédito: R$%.2f' %(saldoMedio, valorCredito))