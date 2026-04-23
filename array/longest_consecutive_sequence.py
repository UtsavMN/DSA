class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        i=0
        lenc,maxc=0,0
        num=set(nums)
        for i in num:
            j=0
            lenc=0
            if i-1 not in num:
                while i+j in num:
                    j+=1
                    lenc+=1
            maxc=max(maxc,lenc)
        return maxc    
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
s=Solution()
   
