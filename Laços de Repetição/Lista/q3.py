while True:
    numeroHoras = int(input("Entre com o número de horas trabalhadas (-1 para finalizar): "))
    horaNormal = float(input("Entre com o valor da hora normal do trabalhador (C$00.00): "))

    if numeroHoras == -1:
        break
    elif numeroHoras <= 40:
        valor = numeroHoras * horaNormal
    else:
        valor = (numeroHoras + (numeroHoras / 2)) * horaNormal
    
    print(f"Salário: ${valor:.2f}")