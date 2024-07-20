valorEmprestimo = float(input('Informe o valor do empréstimo: '))
salarioCliente = float(input('Informe o seu salário: '))
quantMeses = int(input('Informe a quantidade de meses para pagar: '))

porcentSal = (salarioCliente*(30/100))
valorPrestacao = (valorEmprestimo/quantMeses)

if valorPrestacao > porcentSal:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')