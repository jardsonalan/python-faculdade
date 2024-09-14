def opcaoMenu():
    print('-'*20+'Menu'+'-'*20)
    print('0 - Sair')
    print('1 - A vista com 10%% de desconto')
    print('2 - Em duas vezes (preço da etiqueta)')
    print('3 - de 3 até 10 vezes com 3%% de juros ao mês (somente para compras acima de R$100,00)')
    opcao = int(input('\nInforme a opção: '))
    return opcao

def aVista(valor):
    desconto = valor-(valor * 0.10)
    resultado = print(f'Total a pagar: R${desconto:.2f}')
    return resultado

def duasVezes(valor):
    dividir = valor / 2
    resultado = print(f'Total a pagar: 2x | R${dividir:.2f}')
    return resultado

def acimaValor(valor, vezes):
    dividir = valor / vezes
    valor = dividir
    for i in range(vezes):
        valor += (valor * 0.03)
        print(f'{i+1}° mês: R${valor:.2f}')

def main():
    opcao = 1

    while opcao != 0:
        opcao = opcaoMenu()
        if opcao <= 0:
            break
        else:
            valorProduto = float(input('Valor do produto: '))
            if opcao == 1:
                aVista(valorProduto)
            
            elif opcao == 2:
                duasVezes(valorProduto)

            elif opcao == 3:
                if valorProduto > 100:
                    totalVezes = int(input('Em quantas vezes (3 até 10): '))
                    if totalVezes >= 3 and totalVezes <= 10:
                        acimaValor(valorProduto, totalVezes)
                    else:
                        print('Quantidade inválida.')
                else:
                    print('Valor abaixo.')

main()