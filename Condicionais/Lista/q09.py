valorX = float(input('Informe o valor de X: '))

if valorX <= 1:
    print('Valor de f(x): 1')
elif valorX > 1 and valorX <= 2:
    print('Valor de f(x): 2')
elif valorX > 2 and valorX <= 3:
    novoValor = valorX**2
    print('Valor de f(x): %.2f' %novoValor)
else:
    novoValor = valorX**3
    print('Valor de f(x): %.2f' %novoValor)