'''Find Nth root of a number
Subscribe to TUF+
Hints
Company
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
Example 1
Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.
Example 2
Input: N = 4, M = 69
Output:-1
Explanation: The 4th root of 69 does not exist. So, the answer is -1.

Constraints

  1 <= N <= 30
  1 <= M <= 109'''
class Solution:
    def NthRoot(self, n, m):
         for i in range(1,m+1):
            if i**n==m:
                return i
            if i**n>m:
                break
         return -1
n=int(input('enetr the value of n'))
m=int(input('enetr the value of m'))
s=Solution()
print("nth root is:",s.NthRoot(n,m))