# Questão 5
par = []
impar = []
listaCompleta = []

for i in range(5):
    numero = int(input(f"Informe o {i+1}° número inteiro: "))
    listaCompleta.append(numero)

    if numero % 2 == 0:
        par.append(numero)
        
    elif numero % 2 != 0:
        impar.append(numero)

maiorPar=0
i=0
while i < len(par):
    if par[i] > maiorPar:
        maiorPar = par[i]
    else:
        pass
    i+=1

impar.sort()
menorImpar = impar[0]

i=0
soma=0
while i < len(listaCompleta):
    soma+=listaCompleta[i]
    i+=1

print(f'A soma dos elementos é igual a: {soma}')
print(f'A média é igual: {soma/2}')
print(f'O maior par é: {maiorPar}')
print(f'O menor ímpar é: {menorImpar}')