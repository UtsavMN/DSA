arr=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=int(input("enetr the rows"))
m=1
for i in range(n):
    for j in arr[:m]:
        print(j,end="")
    m+=1
    print("")