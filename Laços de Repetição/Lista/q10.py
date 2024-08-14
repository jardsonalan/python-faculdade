listLitro = 0
repeticoes = 0
while True:
    litros = float(input("Entre com os litros consumidos (-1 para finalizar): "))
    if litros == -1:
        mediaKmL = listLitro / repeticoes
        print(f"A taxa total de km/litro foi: {mediaKmL:.6f}")
        break
    else:
        km = float(input("Entre com os km percorridos: "))
        taxaKmL = km / litros
        listLitro += taxaKmL
        repeticoes += 1
        print(f"A taxa km/litro para esse tanque foi: {taxaKmL:.6f}")