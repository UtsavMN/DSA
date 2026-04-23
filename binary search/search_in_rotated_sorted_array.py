class Solution(object):
    def search(self, nums, k):
        n=len(nums)
        l=0
        h=n-1
        pos=0
        mid=(l+h)//2
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==0:
                pos=mid
                return pos
            elif nums[mid]>0:
                l=mid+1
            else:
                h=mid-1
        mid=pos
        return pos
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
k=int(input('enetr the target element'))
s=Solution()
print("present in the index:",s.search(nums,k))