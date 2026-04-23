class Solution(object):
    def singleNonDuplicate(self, nums):
        l=0
        h=len(nums)
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==nums[mid+1]:
                l=mid+1
            elif nums[mid]==nums[mid-1]:
                h=mid
            else:
                return nums[mid]
        return nums[mid]
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
s=Solution()
print("single element is:",s.singleNonDuplicate(nums))