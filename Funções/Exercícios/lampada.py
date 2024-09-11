def exibeOpcoes():
    print('#### MENU ####\n')
    print('0 - SAIR')
    print('1 - ACENDER LUZ')
    print('2 - APAGAR LUZ')
    print('3 - CONSULTAR ESTADO ATUAL')
    opcao = int(input('Escolha a opção que deseja: '))
    return opcao

def acenderLampada():
    estado = 'Acesa'
    return estado

def apagarLampada():
    estado = 'Apagada'
    return estado

def exibirStatus(estadoAtual):
    print(f'O estado atual da lâmpada: {estadoAtual}\n')

opcao=1
estado='Apagada'

while opcao != 0:
    opcao = exibeOpcoes()

    if opcao <= 0:
        break
    
    elif opcao == 1:
        estado = acenderLampada()
        print(f'Estado da lâmpada: {estado}\n')
    
    elif opcao == 2:
        estado = apagarLampada()
        print(f'Estado da lâmpada: {estado}\n')

    elif opcao == 3:
        exibirStatus(estado)