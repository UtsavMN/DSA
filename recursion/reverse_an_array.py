class Solution:
    def reverse(self, arr: list, n: int):
        rev=list(reversed(arr))
        return rev
if __name__=="__main__":

    n=int(input("Enter the number of elements in the array: "))
    arr=[]
    for i in range(n):
        arr.append(int(input("enetr the element: ")))
    s=solution=Solution()
    rev=s.reverse(arr,n)
    print(rev)
        