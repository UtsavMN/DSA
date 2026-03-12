def fibi(n):
    if n<=1:
        return n
    else:
        return fibi(n-1)+fibi(n-2)
n=int(input("enter the number"))
print(fibi(n))