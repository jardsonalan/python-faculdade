while True:
    entrada=float(input("Entre com a venda em dólares (-1 para finalizar): "))
    if entrada == -1:
        break
    else:
        valor = (entrada * (9/100) + 200)
        print(f"Salário: ${valor:.2f}")