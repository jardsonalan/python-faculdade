a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

resultado = []

for i in range(10):
    mult = (a[i] * b[i])
    resultado.append(mult)

for n in resultado:
    print(n)