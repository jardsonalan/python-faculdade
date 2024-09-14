qtdAlunos = int(input('Informe a quantidade de alunos: '))

notas = []

for i in range(qtdAlunos):
    notaAluno = int(input(f'Informe a {i+1}° nota: '))
    notas.append(notaAluno)

contador = 0
aux = 0

for c in notas:
    if contador == 0:
        for b in notas:
            if b == c:
                contador += 1
    if aux != c:
        print(f"A nota {c} aparece: {contador} vezes.")
        
    aux = c
    contador = 0

# Falta terminar