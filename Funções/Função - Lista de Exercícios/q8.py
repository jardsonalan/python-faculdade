def fatorial(numero):
    contador = 1
    for i in range(1, numero + 1):
        contador *= i
    resultado = print(f'O fatorial do número {numero} é: {contador}')
    return resultado

num = int(input('Informe o número que deseja fatorar: '))

fatorial(num)