listaNum=[]

for i in range(10):
    num = int(input('Informe um número: '))

    if num % 2 == 0:
        listaNum.append(1)
    else:
        listaNum.append(-1)

i=0
print('-'*40)
while i < len(listaNum):
    print(listaNum[i])
    i+=1
print('-'*40)