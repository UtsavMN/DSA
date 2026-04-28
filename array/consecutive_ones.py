class Solution:
    def findMaxConsecutiveOnes(self, num):
        n=len(num)
        maxc=0
        c=0
        for i in num:
            if i==1:
                c+=1
            else:
                maxc=max(c,maxc)
                c=0
        maxc=max(c,maxc)
        return maxc
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
x=s.findMaxConsecutiveOnes(num)
print(x)        