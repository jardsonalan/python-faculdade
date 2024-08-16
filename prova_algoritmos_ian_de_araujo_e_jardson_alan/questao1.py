# Nome: Ian de Araújo Galvão
# Nome: Jardson Alan Vieira da Silva

soma_pares = 0
numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    if c % 2 == 0:
        soma_pares = soma_pares + c
print(f"A soma dos números pares é igual a: {soma_pares}")