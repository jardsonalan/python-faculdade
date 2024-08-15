contador = 0
maior1 = 0
maior2 = 0
numAnterior = 0

while contador < 10:
    num = int(input(f"Informe o {contador+1}º número: "))
    if num > maior2:
        numAnterior = maior2
        maior2 = num
        maior1 = numAnterior
        contador += 1
    elif maior1 < maior2 and num > maior1:
        maior1 = num
        contador += 1
    elif num < maior1 and num < maior2:
        contador += 1
    elif num == maior2 or num == maior1:
        print("Informe outro número")
        contador
        
    print(f"O primeiro maior número: {maior2}\nO segundo maior número: {maior1}")
