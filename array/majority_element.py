#this is not an optimal solution this has mor time compleexity than the Boyer-Moore algo
class Solution:
    def majorityele(self, num):
        n=len(num)
        maxc=0
        c=0
        k=num[0]
        for i in num:
            for j in num:
                if i==j:
                    c+=1
            if c>maxc:
             k=i
             maxc=c
            c=0
        return k
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
x=s.majorityele(num)
print(x)        