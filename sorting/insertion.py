'''Insertion Sorting
Subscribe to TUF+
Hints
Company
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
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
    def insertionSort(self, nums):
        self.nums=nums
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
        return nums
            
n=int(input("Enter the number of elements in the array: "))
nums=[]
for i in range(n):
    nums.append(int(input("enter the element: ")))
s=Solution()
print(s.insertionSort(nums))        