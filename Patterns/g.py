n=int(input("enetr the rows"))
m=n
k=n
x=0
for i in range(n):
    for j in range(m):
        print(" ",end="")    
    for b in range(k):
        print("*",end="")
    for p in range(k-1):
        print("*",end="")
    k=k-1
    m+=1
    print()