k = []

for i in range(30):
    num = int(input(f'Informe o {i+1}° número: '))
    k.append(num)

aux = 0

for a in range(30):
    if k[a] % 2 != 0:
        aux = k[a]
    
    if k[a] % 2 == 0:
        if aux % 2 == 0:
            k[a] = k[a]
        else:
            k[a-1] = k[a]
            k[a] = aux

print(k)