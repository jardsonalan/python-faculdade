s = []

for i in range(20):
    num = int(input(f"Informe o {i+1}° número: "))
    s.append(num)

a = int(input('Deseja multiplicar a lista por quanto: '))

for c in s:
    print(c*a)