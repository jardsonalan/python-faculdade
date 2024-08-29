qtd_alunos = int(input("Informe a quantidade de alunos: "))

aprovado = []
reprovado = []

for i in range(1, qtd_alunos+1):
    nota = float(input(f"Nota do {i}° aluno: "))

    if nota >= 60 and nota <= 100:
        aprovado.append(nota)
    elif nota < 60:
        reprovado.append(nota)
    
print(f'O total de alunos acima da média é: {len(aprovado)}')
print(f'O total de alunos abaixo da média é: {len(reprovado)}')