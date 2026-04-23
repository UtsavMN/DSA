class Solution(object):
    def removeOuterParentheses(self, s):
        res=''
        b=0
        for i in s:
            if i=='(':
                if b>0:
                    res+='('
                b+=1
            else:
                b-=1
                if b>0:
                    res+=')'
        return res

n=int(input('enetr the number of elements'))
s=input("enetr the ele")
s=Solution()
print(s.removeOuterParentheses(s))
