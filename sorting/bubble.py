'''Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
Example 1
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]
Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.
Example 2
Input: nums = [5, 4, 4, 1, 1]
Output: [1, 1, 4, 4, 5]
Explanation: 1 <= 1 <= 4 <= 4 <= 5.
Thus the array is sorted in non-decreasing order.'''
class Solution:
    def bubbleSort(self, nums, n):
        self.nums=nums
        k=1
        if(k>n):
            return nums
        k+=1
        self.bubbleSort(nums,n)
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
        i+=1
n=int(input("Enter the number of elements in the array: "))
nums=[]
for i in range(n):
    nums.append(int(input("enter the element: ")))
s=Solution()
print(s.bubbleSort(nums,n))