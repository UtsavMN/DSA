class Solution(object):
    def searchInsert(self, nums, k):
        n=len(nums)
        l=0
        h=n-1
        mid=(l+h)//2
        while nums[mid]!=k:
            mid=(l+h)//2
            if nums[mid]==k:
                return mid 
            if nums[mid]>k:
                h=mid-1
            else:
                l=mid+1
            if l==mid or h==mid:
                if nums[mid]>k:
                    return mid
                else :
                    return mid+1      
        return mid 
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
k=int(input('enetr the target element'))
s=Solution()
print("present in the index:",s.searchInsert(nums,k))

