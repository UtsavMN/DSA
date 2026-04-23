class Solution(object):
    def search(self, num, k):
        n=len(num)
        l=0
        h=n-1
        mid=(l+h)//2
        while num[mid]!=k:
            mid=(l+h)//2
            if num[mid]==k:
                return mid
            if num[mid]>k:
                h=mid-1
            else:
                l=mid+1
            if l==mid or h==mid:
                print("element not found")
                return -1
        return mid
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
k=int(input('enetr the target element'))
s=Solution()
print("present in the index:",s.search(num,k))