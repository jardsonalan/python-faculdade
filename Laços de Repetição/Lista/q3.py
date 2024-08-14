while True:
    numeroHoras = int(input("Entre com o número de horas trabalhadas (-1 para finalizar): "))

    if numeroHoras == -1:
        break
    elif numeroHoras <= 40:
        horaNormal = float(input("Entre com o valor da hora normal do trabalhador (C$00.00): "))
        valor = numeroHoras * horaNormal
    else:
        horaNormal = float(input("Entre com o valor da hora normal do trabalhador (C$00.00): "))
        valor = (numeroHoras + (numeroHoras / 2)) * (horaNormal - (horaNormal % 4))
    
    print(f"Salário: ${valor:.2f}")