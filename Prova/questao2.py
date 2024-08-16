# Nome: Ian de Araújo Galvão
# Nome: Jardson Alan Vieira da Silva

n = int(input("Informe um número ou digite (-1) para encerrar: "))
a = 0
b = 0
c = 0
for i in range(n):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        a = i
        a,b = b, b+a
        print(b)