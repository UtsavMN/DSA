class Solution(object):
    def isIsomorphic(self, s, t):
        i=0
        j=0
        while i < len(s):
            s=s.replace(s[i],str(i))
            t=t.replace(t[i],str(i))
            i+=1
        while j<len(s):
            if s[j]==t[j]:
                j+=1
            else:
                return False
            if j==len(s)-1:
                return True
        return True
s=str(input("enetr the string"))
t=str(input("enetr the string"))
x=Solution()
print(x.isIsomorphic(s,t))