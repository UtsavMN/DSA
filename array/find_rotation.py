class Solution:
    def findKRotation(self, nums):
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]>nums[h]:
                l=mid+1
            else:
                h=mid
        return n-l
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
s=Solution()
print("number of times the array is rotated:",s.findKRotation(nums))