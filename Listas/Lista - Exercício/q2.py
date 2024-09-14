listaNum=[]

for i in range(10):
    num = int(input('Informe um número: '))
    listaNum.append(num)

for c in range(10):
    if listaNum[c] % 2 == 0:
        listaNum[c] = 1
    else:
        listaNum[c] = -1

print('-'*40)
for b in listaNum:
    print(b)
print('-'*40)