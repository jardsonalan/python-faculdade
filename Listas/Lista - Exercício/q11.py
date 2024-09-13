qtdAlunos = int(input('Informe a quantidade de alunos: '))

notas = []

for i in range(qtdAlunos):
    notaAluno = int(input(f'Informe a {i+1}° nota: '))
    notas.append(notaAluno)

contador = 0

for c in notas:
    contador = 0
    for b in notas:
        if b == c:
            contador += 1

    print(f"A nota {c} aparece: {contador} vezes.")