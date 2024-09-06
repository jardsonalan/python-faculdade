a = []

qtd_numeros = int(input('Informe a quantidade de números que deseja na lista: '))

for i in range(qtd_numeros):
    num = int(input("Informe um número: "))
    a.append(num)

busca = int(input("Qual número deseja buscar: "))
retorno = a.count(busca)
print(f'O número ({busca}) aparece: {retorno}')