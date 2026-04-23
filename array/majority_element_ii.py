#this is not an optimal solution this has mor time compleexity than the Boyer-Moore algo
class Solution:
    def majorityele(self, num):
        n=len(num)
        b=n/3
        arr=[]
        c=0
        k=num[0]
        for i in num:
            for j in num:
                if i==j:
                    c+=1
            if c>b:
             arr.append(i)
            c=0
        return list(set(arr))
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
x=s.majorityele(num)
print(x)        