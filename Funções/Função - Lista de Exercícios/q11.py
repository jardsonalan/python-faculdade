import math

def numerosPrimos(m):
    if m <= 2:
        return False
    
    elif m == 2:
        return True
    
    elif m % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(m)+1), 2):
        if m % i == 0:
            return False
    
    return True

def somaPrimos(n):
    soma = 0
    numero = 2

    for i in range(n):
        if numerosPrimos(numero):
            soma += numero
        numero += 1
    
    return soma

def main():
    num = int(input('Informe um número: '))
    if num < 0:
        print('Informe um número positivo.')
    else:
        resultado = somaPrimos(num)
        print(f'A soma dos números primos até {num} é: {resultado}')

main()