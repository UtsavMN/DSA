class Solution(object):
    def rearrangeArray(self, num):
        p = 0
        n = 0
        flag = 0   # 0 → expect positive, 1 → expect negative
        temp = []
        length = len(num)

        while len(temp) < length:
            
            # find next positive
            while p < length and num[p] < 0:
                p += 1

            # find next negative
            while n < length and num[n] > 0:
                n += 1

            if flag == 0 and p < length:
                temp.append(num[p])
                p += 1
                flag = 1

            elif flag == 1 and n < length:
                temp.append(num[n])
                n += 1
                flag = 0

        return temp
n=int(input('enetr the number of elements'))
num=[]
for i in range(n):
    num.append(int(input("enetr the ele")))
s=Solution()
print(s.rearrangeArray(num))