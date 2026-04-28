n=int(input("enter the no of rows"))
m=1
k=1
x=1
for i in range(n):
    for j in range(m):
        print(k,end="")
        if k==1:
          k=0
        else:
          k=1
    m+=1
    if x==1:
        x=0
        k=0
    else:
        x=1
        k=1
    print("")