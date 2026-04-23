class Solution:
    def longestSubarray(self, nums, k):
        f=-1
        n=len(nums)
        r=-1
        sum=0
        lenc=0
        while f<=r and r<n-1:
            if sum<=k:
                r+=1
                print(r)
                sum=sum+nums[r]
                if sum==k:
                    lenc=max(lenc,(r-f)+1)
            elif sum>k:
                f+=1
                sum=sum-nums[f]
                print(f)
        return lenc
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
k=int(input("enter the k value"))
s=Solution()
x=s.longestSubarray(nums,k)
print("longest subarray with sum k is:",x)