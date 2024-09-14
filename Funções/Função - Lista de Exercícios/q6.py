def conversor(metros):
    converter = metros * 100
    resultado = print(f'{metros}m corresponde a {converter}cm.')
    return resultado

valor = float(input('Informe o valor (em metros): '))
conversor(valor)