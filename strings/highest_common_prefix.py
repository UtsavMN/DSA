class Solution(object):
    def longestCommonPrefix(self, strs):
        i=0
        j=0
        minc=min(strs,key=len)
        n=len(minc)
        temp=""
        while j<n:
            while i<len(strs)-1:
                if strs[i][j]==strs[i+1][j]:
                    i+=1
                else:
                    return temp
            if i==len(strs)-1:
                temp+=strs[i][j]
            i=0
            j+=1
        return temp
n=int(input('enetr the number of elements'))
strs=[]
for i in range(n):
    strs.append(input("enetr the ele"))         
                

                
        
        