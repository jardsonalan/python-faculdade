matriz = [[], []]
soma = []

for a in range(2):
    matrizA = int(input(f'Informe o {a+1}° número da Matriz A: '))
    matriz[0].append(matrizA)


for b in range(2):
    matrizB = int(input(f'Informe o {b+1}° número da Matriz B: '))
    matriz[1].append(matrizB)

somaA = (matriz[0][0] + matriz[1][0])
somaB = (matriz[0][1] + matriz[1][1])

print(f'Matriz A: {matriz[0]}')
print(f'Matriz B: {matriz[1]}')

soma.insert(0, somaA)
soma.insert(1, somaB)

print(f'Matriz soma: {soma}')