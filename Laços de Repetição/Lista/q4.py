maior = 0

for contador in range(10):
    num = int(input(f"Informe o {contador+1}º número: "))
    if num > maior:
        maior = num
    
    print(maior)
