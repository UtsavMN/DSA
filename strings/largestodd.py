class Solution(object):
    def largestOddNumber(self, nums):
        for i in range(len(nums)-1,-1,-1):
            if int(nums[i])%2!=0:
                return nums[:i+1]
            elif i==0:
                return ""
nums=str(input("enter the string"))
s=Solution()
print(s.largestOddNumber(nums))