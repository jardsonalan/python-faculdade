# Questão 03
a = []

for i in range(1, 10+1):
    numbers = int(input(f"{i}° número: "))
    a.append(numbers)

a.sort()
print(f'O maior número é: {a[9]}')
print(f'O menor número é: {a[0]}')