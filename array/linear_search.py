class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(num)):
            if num[i]==target:
                return i+1
        return -1
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
target=int(input("enetr the target element"))
k=s.linearSearch(num,target)
if k==-1:
    print("ele not found")
else:
    print(k)