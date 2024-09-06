listaNum=[]

for i in range(10):
    num = int(input("Informe um número: "))
    listaNum.append(num)

i=9
print('-'*40)
while i >= 0:
    print(listaNum[i])
    i-=1
print('-'*40)