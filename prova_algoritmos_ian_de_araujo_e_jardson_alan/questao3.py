# Nome: Ian de Araújo Galvão
# Nome: Jardson Alan Vieira da Silva

c = 0
positivos = 0
negativos = 0
while c < 10:
    c += 1
    numero = int(input(f'Digite o {c} número: '))
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
print(f'Negativos: {negativos} \tPositivos: {positivos}')