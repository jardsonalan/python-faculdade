listaNum = []

positivos = 0
negativo = 0

qtd_numeros = int(input("Informe quantos números deseja armazenar: "))

for i in range(qtd_numeros):
    num = int(input("Informe um número: "))
    listaNum.append(num)

i=0
while i < len(listaNum):
    if listaNum[i] < 0:
        negativo += 1
    else:
        positivos += 1
    i+=1

print('-'*40)
print(f'Positivos: {positivos}')
print(f'Negativos: {negativo}')
print('-'*40)