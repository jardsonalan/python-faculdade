# Nome: Ian de Araújo Galvão
# Nome: Jardson Alan Vieira da Silva

positivos = 0
negativos = 0

for i in range(11):
    n = int(input("Informe 10 números inteiros: "))
    if n < 0:
        negativos = n
    elif n >= 0:
        positivos = n

print(positivos)
print(negativos)