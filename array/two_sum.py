class Solution:
    def twosum(self, num, k):
        arr=[]
        for i in num:
            for j in num:
                if i+j==k:
                    arr.append(i)
                    arr.append(j)
                    return arr
        
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
k=int(input("enter the k value"))
s=Solution()
arr=s.twosum(num,k)
print(arr)