class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        r=[]
        c=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in r:
            for j in range(n):
                matrix[i][j]=0
        for i in c:
            for j in range(m):
                matrix[j][i]=0
        return matrix
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
matrix=s.setZeroes(num)
for row in matrix:
    print(row)