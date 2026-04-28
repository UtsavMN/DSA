n=int(input("enter the rows"))
for i in range(n):
    print("*", end="")
print()
m=1
x=n-1
for i in range(n-2):
    for j in range(m):
        print("*", end="")
    for k in range(x-m):
        print(" ", end="")
    for j in range(m):
        print("*", end="")
    print()
for i in range(n):
    print("*", end="")