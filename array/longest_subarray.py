class Solution:
    def longestSubarray(self, num, k):
        n=len(num)
        maxc=0
        for i in range(n):
            count=0
            sum=0
            for j in range(i,n):
                sum=sum+num[j]
                count+=1
                if sum==k:
                    if count>maxc:
                        maxc=count
        return maxc   
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
k=int(input("enter the k value"))
s=Solution()
arr=s.longestSubarray(num,k)
print("longest subarray with sum k is:",arr)