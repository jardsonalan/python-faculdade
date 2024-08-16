# Nome: Ian de Araújo Galvão
# Nome: Jardson Alan Vieira da Silva

pares = 0

while True:
    n = int(input("Informe um número ou digite (-1) para encerrar: "))
    if n % 2 == 0:
        pares += n
    elif n == -1:
        print(f"A soma dos números pares: {pares}")
        break