listaA = []
listaB = []

print('-'*20+'Lista A'+'-'*20)
for a in range(10):
    numA = int(input(f'Informe o {a+1}° número da lista A: '))
    listaA.append(numA)

print('')
print('-'*20+'Lista B'+'-'*20)
for b in range(10):
    numB = int(input(f'Informe o {b+1}° número da lista B: '))
    listaB.append(numB)

resultado = []

for i in range(10):
    mult = (listaA[i] * listaB[i])
    resultado.append(mult)

print('')
print('-'*20+'Resultado'+'-'*20)
for n in resultado:
    print(n)