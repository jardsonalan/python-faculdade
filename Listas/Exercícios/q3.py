# Questão 03
a = []

for i in range(1, 10+1):
    numbers = int(input(f"{i}° número: "))
    a.append(numbers)

a.sort()
print(f'O maior número é: {a[9]}')
print(f'O menor número é: {a[0]}')

# Outra maneira de resolver

a = []

num = int(input("Informe quantos números deseja adicionar na lista: "))

for i in range(1, num+1):
    numbers = int(input(f"{i}° número: "))
    a.append(numbers)

a.sort()
print(a)
print(f'O maior número é: {a[(len(a)-1)]}')
print(f'O menor número é: {a[0]}')