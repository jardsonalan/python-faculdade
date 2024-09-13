a = []

qtd_numeros = int(input('Informe a quantidade de números que deseja na lista: '))

for i in range(qtd_numeros):
    num = int(input("Informe um número: "))
    a.append(num)

busca = int(input("Qual número deseja buscar: "))

totalVezes = 0

for c in a:
    if busca == c:
        totalVezes += 1
    
print(f"O número {busca} aparece: {totalVezes}")