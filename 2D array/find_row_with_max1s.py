class Solution:
    def rowWithMax1s(self, mat):
        m=len(mat)
        n=len(mat[0])
        lenc,maxc=0,0
        for i in range(m):
            maxc=max(maxc,lenc)
            lenc=0
            for j in range(n):
                if mat[i][j]==1:
                    lenc+=1
        if maxc==0:
            return -1
        return maxc
n=int(input('enetr the number of rows'))
m=int(input('enetr the number of columns'))
num=[]
for i in range(n):
    row=list(map(int,input().split()))
    if len(row)!=m:
        print("invalid input")
        exit()
    num.append(row)
s=Solution()
print("row with maximum 1s is:",s.rowWithMax1s(num))
            