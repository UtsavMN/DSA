'''Sort an array of 0's 1's and 2's
Subscribe to TUF+
Hints
Company
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.
Example 1
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation:
The nums array in sorted order has 2 zeroes, 2 ones and 1 two
Example 2
Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation:
The nums array in sorted order has 2 zeroes, 3 ones and zero twos'''
class Solution:
    def sortZeroOneTwo(self, num):
        low=0
        mid=0
        high=n-1  
        while mid<=high:
            if num[mid]==0:
                num[low],num[mid]=num[mid],num[low]
                low+=1
                m+=1
            elif num[mid]==2:
                num[mid],num[high]=num[high],num[mid]
                high-=1
            else:
                mid+=1
        return num
n=int(input("Enter the number of elements in the array: "))
nums=[]
for i in range(n):
    nums.append(int(input("enter the element: ")))
s=Solution()
print(s.sortZeroOneTwo(nums))     
