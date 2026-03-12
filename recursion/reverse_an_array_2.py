class Solution:
    def reverse(self, arr: list, n: int,left:int,right:int):
        if left>=right:
            return arr
        arr[left],arr[right]=arr[right],arr[left]
        return self.reverse(arr,n,left+1,right-1)
if __name__=="__main__":

    n=int(input("Enter the number of elements in the array: "))
    arr=[]
    left=0
    right=n-1
    for i in range(n):
        arr.append(int(input("enetr the element: ")))
    s=solution=Solution()
    rev=s.reverse(arr,n,left,right)
    print(rev)
        