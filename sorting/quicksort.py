class Solution:
    def swap(self, num, i, j):
        temp = num[i]
        num[i] = num[j]
        num[j] = temp

    def partition(self, num, low, high):
        j = high - 1
        i = low
        while i <= j:
            while i <= j and num[i] < num[high]:
                i += 1
            while i <= j and num[j] > num[high]:
                j -= 1
            if i < j:           # only swap if pointers haven't crossed
                self.swap(num, i, j)
                i += 1
                j -= 1
            elif i == j:        # both point at same element, advance past it
                i += 1
                break
        self.swap(num, i, high) # place pivot at its correct position
        return i

    def quicksort(self, num, low, high):
        if low < high:
            pi = self.partition(num, low, high)
            self.quicksort(num, low, pi - 1)
            self.quicksort(num, pi + 1, high)

n = int(input('Enter the number of elements: '))
num = []
for i in range(n):
    num.append(int(input("Enter the element: ")))

s = Solution()
s.quicksort(num, 0, n - 1)
print(num)