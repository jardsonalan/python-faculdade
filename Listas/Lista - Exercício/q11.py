qtdAlunos = int(input('Informe a quantidade de alunos: '))

notas = []

for i in range(qtdAlunos):
    notaAluno = int(input(f'Informe a {i+1}° nota: '))
    notas.append(notaAluno)

for c in notas:
    qtdVezes = notas.count(c)
    print(F'A nota {c} apareceu: {qtdVezes}')