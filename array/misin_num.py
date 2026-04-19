class Solution:
    def missingNumber(self, num):
        n=len(num)
        small=num[0]
        big=num[0]
        miss=[]
        for i in range(n):
            if num[i]<small:
                small=num[i]
            if num[i]>big:
                big=num[i]
        for i in range(small,big+1):
            if i not in num:
                miss.append(i)
        return miss

n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
miss=s.missingNumber(num)
print(miss)        