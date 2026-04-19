class Solution:
    def dup(self,num):
        return list(set(num))
                    
    def unionArray(self, num1, num2):
        num=[]
        i,j=0,0
        if len(num1)>len(num2):
            n=len(num1)
        else:
            n=len(num2)
        while i<len(num1) and j<len(num2):
            if num1[i]<num2[j]:
                num.append(num1[i])
                i+=1
            else:
                num.append(num2[j])
                j+=1
        while i<len(num1):
            num.append(num1[i])
            i+=1
        while j<len(num2):
            num.append(num2[j])
            j+=1
        return num
n1=int(input('enetr the number of elements'))
num1=[]
for i in range(n1):
    num1.append(int(input("enetr the ele")))
n2=int(input('enetr the number of elements'))
num2=[]
for i in range(n2):
    num2.append(int(input("enetr the ele")))
s=Solution()
num=s.unionArray(num1,num2)
num=s.dup(num)
print(num)