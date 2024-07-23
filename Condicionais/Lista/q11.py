primeiroBimestre = float(input('Primeira nota: '))
segundoBimestre = float(input('Segunda nota: '))
terceiroBimestre = float(input('Terceira nota: '))
quartorBimestre = float(input('Quarta nota: '))

frequencia = int(input('Informe a frequência (0 a 100%): '))

media = ((primeiroBimestre+segundoBimestre+terceiroBimestre+quartorBimestre)/4)

print('-'*40)
print('Média: %.2f' %media)
print('-'*40)

if frequencia <= 75:
    print('Reprovado')
elif frequencia > 75 and frequencia <= 100 and media <= 3:
    print('Reprovado')
elif frequencia > 75 and frequencia <= 100 and media > 3 and media < 7 and primeiroBimestre >= 3 and segundoBimestre >= 3 and terceiroBimestre >= 3 and quartorBimestre >= 3:
    print('4° Prova')
elif frequencia > 75 and frequencia <= 100 and media >= 7 and media <= 10:
    print('Aprovado')