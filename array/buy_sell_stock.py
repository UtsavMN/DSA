class Solution(object):
    def maxProfit(self, prices):
        maxc=0
        minc=prices[0]
        for i in range(len(prices)):
            if prices[i]<minc:
                minc=prices[i]
            if prices[i]-minc>maxc:
                maxc=prices[i]-minc
        return maxc
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
x=s.maxProfit(num)
print(x)