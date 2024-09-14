qtdAlunos = int(input('Informe a quantidade de alunos: '))

notas = []

for i in range(qtdAlunos):
    notaAluno = int(input(f'Informe a {i+1}° nota (0 até 100): '))
    if notaAluno >= 0 and notaAluno <= 100:
        notas.append(notaAluno)

contador = 0
aux = 0

for c in range(len(notas)):
    if contador == 0:
        for b in range(len(notas)):
            if notas[b] == notas[c]:
                contador += 1
    
    if aux != notas[c]:
        print(f"A nota {notas[c]} aparece: {contador} vezes.")

    
    aux = notas[c-1]
    contador = 0