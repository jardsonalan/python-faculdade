import math

def inteiroPositivo(m):
    primo = True

    if m <= 1:
        primo = False
    
    elif m == 2:
        primo = True
    
    elif m % 2 == 0:
        primo = False

    else:
        for i in range(3, int(math.sqrt(m)+1), 2):
            if m % i == 0:
                primo = False
                break

    if primo:
        print(1)
    else:
        print(0)

def main():
    num = int(input('Informe um número: '))
    if num < 0:
        print('Informe um número positivo.')
    else:
        inteiroPositivo(num)

main()