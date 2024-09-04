# # Exemplo 1

# umaLista = []
# umaLista.append("Joãozinho")
# umaLista.append("Chico de José")
# umaLista.append("Antônio")
# umaLista.append("Zefinha")

# i=0

# while i<len(umaLista):
#     print(umaLista[i])
#     i+=1

# # Exemplo 2

# suaLista = ['algoritmo', 'é', 'muito', 'legal']
# suaLista.insert(2, 'de verdade')

# i = 0

# while i < len(suaLista):
#     print(suaLista[i])
#     i+=1

# # Exemplo 3

# alunos = []

# qtdAlunos = int(input('Informe a quantidade de alunos na turma: '))
# i=0
# while i < qtdAlunos:
#     nome = input(f'Informe o nome do {i+1}° aluno: ')
#     alunos.append(nome)
#     i+=1

# print('\n\n================ LISTA DE ALUNOS ================')
# i=0
# while i < qtdAlunos:
#     print(f'Aluno {i+1}: {alunos[i]}')
#     i+=1

# # Exemplo 4

# suaLista = [10, 50, 5, 2, 100]
# del suaLista[2]

# i=0
# while i < len(suaLista):
#     print(suaLista[i])
#     i+=1

# # Exemplo 5

# suaLista = [10,50,5,2,100]

# elementoRemovido = suaLista.pop(2)
# print(f'Removido: {elementoRemovido}')

# i=0
# while i < len(suaLista):
#     print(suaLista[i])
#     i+=1

# # Exemplo 6

# suaLista = [10,50,5,2,100]

# suaLista.remove(5)

# i=0
# while i < len(suaLista):
#     print(suaLista[i])
#     i+=1

# # Exemplo 7
# suaLista = ['algoritmo', 'é', 'muito', 'legal']

# suaLista.remove('muito')

# i=0
# while i < len(suaLista):
#     print(suaLista[i])
#     i+=1

# # Exemplo 8

# suaLista = [10,50,5,2,100]

# tamanho = len(suaLista)
# print(f"O tamanho da lista é: {tamanho}")

# Exemplo 9

suaLista = [10,50,5,2,100]

i=0
while i < len(suaLista):
    print(suaLista[i])
    i+=1

# Exemplo 10

suaLista = [10,50,5,2,100]

for i in suaLista:
    print(i)