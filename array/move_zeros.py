class Solution:
    def swap(self,num,i):
        for k in range(i,n-1):
            num[k]=num[k+1]
    def moveZeroes(self, num):
        n=len(num)
        j=n-1
        count=0
        for i in range(n):
            if num[i]==0:
                count+=1
                self.swap(num,i)
        for i in range(count):
            num[n-i-1]=0
        return num
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
s.moveZeroes(num)
print(num)