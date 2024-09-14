numeros = []

pares = 0

for p in range(20):
    num = int(input(f'Informe o {p+1}° número: '))
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        pares += 1

print(f'Total de números pares: {pares}')