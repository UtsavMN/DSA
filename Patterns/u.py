n=int(input("enter the rows"))
def prt(n):
    if n<=0:
        return
    a=n+2
for i in range(a+1):
    print(n, end="")
print()
m=1
x=a
for i in range(a-1):
    for j in range(m):
        print(n, end="")
    for k in range(x-m):
        print(" ", end="")
    for j in range(m):
        print(n, end="")
    print()
for i in range(a+1):
    print(n, end="")
n=n-1
