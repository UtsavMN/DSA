class Palindrome:    
    def palindromeCheck(self, s):
        if len(s)==1 or len(s)==0:
            print("The string is a palindrome")
            return True
        for i in range(len(s)):
            if s[i]!=s[len(s)-1-i]:
                print("the string is not palindrome")
                return False
        print("the string is a palindrome")
str=input("Enter the string: ")
s=Palindrome()
s.palindromeCheck(str)