'''Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.
Example 1
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]
Explanation:
2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]
Example 2
Input: nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]
Explanation:
-5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]
Now your turn!
Input: nums = [-3, 4, 5, 1, -30, -10]
Output:
Pick your answer
[-3, 4, 5]
[5, 1, -30]
[5, 1, -10]
[5, -10, 1]
Constraints
1 <= nums.length <= 105
-104 <= nums[i] <= 104'''

class Solution:
    def leaders(self, nums):
        pst=float('-inf')
        n=len(nums)
        r=n-1
        arr=[]
        while r>=0:
            if nums[r]>pst:
                arr.append(nums[r])
                pst=nums[r]
                r-=1
            else:
                r-=1
        return arr[::-1]
n=int(input('enetr the number of elements'))
nums=[]
for i in range(n):
    nums.append(int(input("enetr the ele")))
s=Solution()
print(s.leaders(nums))


