class Solution(object):
    def minEatingSpeed(self, piles, h):
        hi=max(piles)
        l=1
        hours=0
        y=0
        opt= float('inf')
        while l<=hi:
            k=(l+hi)//2
            hours=0
            for i in piles:
                if i%k==0:
                    hours=hours+i//k
                else:
                    hours=hours+((i//k)+1)
            x=h-hours
            if x >= 0:
                if x < opt or (x == opt and k < y):
                    opt = x
                    y = k
                hi = k - 1
            else:
                l = k + 1

        return y
n=int(input('enetr the number of piles'))
piles=[]
for i in range(n):
    piles.append(int(input("enetr the ele")))
h=int(input('enetr the hours'))
s=Solution()
print("minimum eating speed:",s.minEatingSpeed(piles,h))