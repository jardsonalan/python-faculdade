n = 1
print("N \tN*10 \tN*100 \tN*1000")

while n <= 10:
    n10 = 10*n
    n100 = 100*n
    n1000 = 1000*n
    print("%d \t%d \t%d \t%d" %(n, n10, n100, n1000))
    n+=1