lista = []

for i in range(15):
    num = int(input(f'Informe o {i+1}° número: '))
    lista.append(num)

aux = 0

for c in range(15):
    for d in range(15 - c - 1):
        if lista[d] > lista[d+1]:
            aux = lista[d]
            lista[d] = lista[d+1]
            lista[d+1] = aux

print('')
for e in lista:
    print(e)