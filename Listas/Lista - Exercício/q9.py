lista = []

for i in range(20):
    num = int(input(f'Informe o {i+1}° número: '))
    lista.append(num)

print('')
for b in lista:
    print(b)

print('')
for e in range(19, -1, -1):
    print(lista[e])