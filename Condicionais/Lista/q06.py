nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = ((nota1+nota2)/2)

if media >= 0 and media <= 3:
    print('Reprovado')
elif media > 3 and media < 7:
    print('Quarta prova')
elif media >= 7:
    print('Aprovado')