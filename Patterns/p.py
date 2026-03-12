n= int(input("enetr the rows below or equal to 5:"))
m=4
arr=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(n):
    for j in arr[m:5]:
        print(j,end="")
    m-=1
    print("")