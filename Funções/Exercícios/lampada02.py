listaLampadas = ['', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada', 'apagada']

def exibeOpcoes():
    print('-'*20+'MENU'+'-'*20)
    print('0 - Sair')
    print('1 - Acender Lâmpada')
    print('2 - Apagar Lâmpada')
    print('3 - Exibir Status da Lâmpada')
    print('4 - Exibir Todas')
    num = int(input('Informe uma opção do menu: '))
    return num

def acenderLampada():
    global lampada
    lampada = True

def apagarLampada():
    global lampada
    lampada = False
    

def exibirStatusLampada(numLampada):
    print(f'Lâmpada {numLampada}: {listaLampadas[numLampada]}')

def exibirTodas():
    for i in range(1, len(listaLampadas)):
        print(f'Lâmpada {i}: {listaLampadas[i]}')

lampada = False

def main():
    num = 1

    while num != 0:
        num = exibeOpcoes()

        if num <= 0:
            break

        elif num == 1:
            posLampada = int(input('Informe qual lâmpada você deseja acender (1-20): '))
            if posLampada <= 0 or posLampada > 20:
                print('Você ultrapassou o tamanho da lista.')
            else:
                acenderLampada()

                if lampada:
                    listaLampadas[posLampada]='acesa'

        elif num == 2:
            posLampada = int(input('Informe qual lâmpada você deseja apagar (1-20): '))
            if posLampada <= 0 or posLampada > 20:
                print('Você ultrapassou o tamanho da lista.')
            else:
                apagarLampada()

                if lampada == False:
                    listaLampadas[posLampada]='apagada'

        elif num == 3:
            posLampada = int(input('Informe qual lâmpada você deseja saber o status (1-20): '))
            if posLampada <= 0 or posLampada > 20:
                print('Você ultrapassou o tamanho da lista.')
            else:
                exibirStatusLampada(posLampada)
        
        elif num == 4:
            exibirTodas()
        
        else:
            print('Opção inválida.')

main()