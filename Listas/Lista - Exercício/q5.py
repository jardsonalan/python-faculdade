pares = []
impares = []

for i in range(30):
    num = int(input("Informe um número: "))

    if num % 2 == 0:
        if len(pares) == 5:
            print('Lista cheia')
            print('-'*40)
            i=0
            while i < len(pares):
                print(pares[i])
                i+=1
            print('-'*40)
        else:
            pares.append(num)
    else:
        if len(impares) == 5:
            print('Lista cheia')
            print('-'*40)
            i=0
            while i < len(impares):
                print(impares[i])
                i+=1
            print('-'*40)
        else:
            impares.append(num)

print('-'*20+'Pares'+'-'*20)
i=0
while i < len(pares):
    print(pares[i])
    i+=1
print('-'*40)

print('-'*20+'Ímpares'+'-'*20)
i=0
while i < len(impares):
    print(impares[i])
    i+=1
print('-'*40)