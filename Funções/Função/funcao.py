# # Exemplo 1

# def quadrado(numero):
#     return numero*numero

# tamanho = 6
# numQuadrado = 0

# for i in range(tamanho):
#     numQuadrado = quadrado(i)
#     print(f'{numQuadrado}')

# Exemplo 2

def quadrado(numero):
    return numero*numero

def imprimeQuadrado (numero):
    if numero <= 1:
        return
    print(f'{quadrado(numero)}')

tamanho = 6
numQuadrado = 0

for i in range(tamanho):
    imprimeQuadrado(i)