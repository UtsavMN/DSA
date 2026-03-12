n=int(input("enetr the rows"))
m=1
k=1
z=1
for i in range(n):
    for j in range(m):
        print(k,end="")
        k+=1
    for j in range(n-m):
        print(" ", end="")
    for j in range(n-m):
        print(" ", end="")
    for j in range(m):
        print(z,end="")
        z-=1
    m+=1
    k=1
    z=m
    print("")