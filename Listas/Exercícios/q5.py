i = 0

maiorPar = []
menorImpar = []
listaCompleta = []

while i < 5:
    numero = int(input(f"Informe o {i}° número inteiro: "))
    listaCompleta.append(numero)

    if numero % 2 == 0:
        maiorPar.append(numero)
        if numero > maiorPar[0]:
            maiorPar.pop(0)
            maiorPar.append(numero)
    elif numero % 2 != 0:
        menorImpar.append(numero)
        if numero < menorImpar[0]:
            menorImpar.pop(0)
            menorImpar.append(numero)
    
    i+=1

i=0
while i < 5:
    elemento = listaCompleta[i]
    somaElementos = elemento + elemento
    i+=1

print(f'A soma dos elementos é igual a: {somaElementos}')
print(f'A média é igual: {somaElementos/2}')
print(f'O maior par é: {maiorPar[0]}')
print(f'O menor ímpar é: {menorImpar[0]}')