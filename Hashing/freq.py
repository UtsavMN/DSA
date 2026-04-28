class Solution:
    def coun(self, nums):
        fre={}
        self.nums=nums
        for i in nums:
            fre[i]=fre.get(i,0)+1
        results=[]
        for key in fre:
            results.append([key,fre[key]])
        return results
nums=[]
n=int(input("Enter the number of elements in the array: "))
for i in range(n):
    nums.append(int(input("enetr the element: ")))
s=solution=Solution()
print(s.coun(nums))
