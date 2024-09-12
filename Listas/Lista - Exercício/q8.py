numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1

print(pares)