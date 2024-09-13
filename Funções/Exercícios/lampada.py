def exibeOpcoes():
    print('#### MENU ####\n')
    print('0 - SAIR')
    print('1 - ACENDER LUZ')
    print('2 - APAGAR LUZ')
    print('3 - CONSULTAR ESTADO ATUAL')
    opcao = int(input('Escolha a opção que deseja: '))
    return opcao

def acenderLampada():
    global lampada
    lampada = True

def exibirStatus():
    global lampada
    if lampada:
        print('Lâmpada acesa')
    else:
        print('Lâmpada apagada')

opcao=1
lampada = False

while opcao != 0:
    opcao = exibeOpcoes()

    if opcao <= 0:
        break
    
    elif opcao == 1:
        acenderLampada()
    
    elif opcao == 2:
        lampada = False

    elif opcao == 3:
        exibirStatus()