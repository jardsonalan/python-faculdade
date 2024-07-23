nota = float(input('Informe a nota (0.0 a 10.0): '))
frequencia = int(input('Informe a frequência (0 a 100%): '))

if frequencia <= 75:
    print('Reprovado')
elif frequencia > 75 and frequencia <= 100 and nota <= 3:
    print('Reprovado')
elif frequencia > 75 and frequencia <= 100 and nota > 3 and nota < 7:
    print('4° Prova')
elif frequencia > 75 and frequencia <= 100 and nota >= 7 and nota <= 10:
    print('Aprovado')