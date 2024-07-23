saldoMedio = float(input('Informe o saldo médio: '))

if saldoMedio <= 500:
    print('Nenhum crédito')
elif saldoMedio >= 501 or saldoMedio <= 1000:
    valorCredito = (saldoMedio*(30/100))*(2/100)
    print('Saldo médio: R$%.2f\nValor de crédito: %.1f%%' %(saldoMedio, valorCredito))
elif saldoMedio >= 1001 or saldoMedio <= 3000:
    valorCredito = (saldoMedio*(40/100))*(2/100)
    print('Saldo médio: R$%.2f\nValor de crédito: %.1f%%' %(saldoMedio, valorCredito))
elif saldoMedio >= 3001:
    valorCredito = (saldoMedio*(50/100))*(2/100)
    print('Saldo médio: R$%.2f\nValor de crédito: %.1f%%' %(saldoMedio, valorCredito))