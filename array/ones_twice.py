class Solution:
    def singleNumber(self, num):
        f=0
        arr=[]
        for i in num:
            for j in num:
                if i==j:
                    f+=1
            if f==1:
                arr.append(i)
            f=0
        return arr
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
arr=s.singleNumber(num)   
print(arr)   