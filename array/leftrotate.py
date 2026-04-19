class Solution:
    def rotateArray(self, num,k):
        n=len(num)
        temp=[n]*k
        j=0
        for i in range(k):
            temp[i]=num[i]
        for i in range(k,n):
            num[j]=num[i]
            j+=1
        for i in range(k):
            num[n-k+i]=temp[i]
        return num
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
k=int(input("enetr the number of times to rotate: "))
s.rotateArray(num,k)
print(num)