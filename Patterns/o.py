n=int(input("enetr the rows"))
m=n
arr=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
k=1
x=1
for i in range(n):
    for t in range(m):
        print(" ",end="")
    for j in arr[:k]:
        print(j,end="")
    for y in reversed(arr[:k-1]):
        print(y,end="")
    k=k+1
    m-=1
    print()

