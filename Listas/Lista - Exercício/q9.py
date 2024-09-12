# numeros = []

# for i in range(20):
#     num = int(input(f'Informe o {i+1}° número: '))
#     numeros.append(num)

# numeros.sort(reverse=True)
# print(numeros)

lista = []

for i in range(20):
    num = int(input(f'Informe o {i+1}° número: '))
    lista.append(num)

for e in range(19, -1, -1):
    print(lista[e])