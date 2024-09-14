lista = []

maiorPar = 0
menorImpar = 0
soma = 0

for i in range(5):
    num = int(input(f'Informe o {i+1}° número: '))
    lista.append(num)

for c in lista:
    if c % 2 == 0 and c >= maiorPar:
        maiorPar = c

if maiorPar == 0:
    print('Nenhum número par foi inserido.')
else:
    print(f'O maior número par é: {maiorPar}')

for b in lista:
    if b % 2 != 0:
        for d in lista:
            if d <= b:
                menorImpar = d
    
    for d in lista:
        if d <= menorImpar and d % 2 != 0:
            menorImpar = d

if menorImpar == 0:
    print('Nenhum número ímpar foi inserido.')
else:
    print(f'O menor número ímpar é: {menorImpar}')

for e in lista:
    soma += e

print(f'O somátorio dos elementos da lista é: {soma}')
print(f'A média dos elementos da lista é igual: {soma/2}')