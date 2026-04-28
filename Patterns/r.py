n=int(input("enetr the rows"))
m=1
for i in range(n):
    for j in range(m):
        print("*",end="")
    for k in range(n-m):
        print(" ", end="")
    for k in range(n-m):
        print(" ", end="")
    for j in range(m):
        print("*", end="")        
    m+=1
    print("")
m=n-1
for i in range(n):
    for j in range(m):
        print("*", end="")
    for k in range(n-m):
        print(" ", end="")
    for k in range(n-m):
        print(" ", end="")
    for j in range(m):
        print("*", end="")
    m-=1
    print()
