lado = int(input("Informe um número de 0 até 20: "))

print("*"*lado)

for i in range(lado-2):
    print("*"+(" "*(lado-2))+"*")

print("*"*lado)