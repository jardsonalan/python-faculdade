def func():
    global x
    x=1
    print(x)

x = 42
print(x)
func()
print(x)