def quadrado(numero):
    return numero*numero

tamanho = 6
numQuadrado = 0

for i in range(tamanho):
    numQuadrado = quadrado(i)
    print(f'{numQuadrado}\t')