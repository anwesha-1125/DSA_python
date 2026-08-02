class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy = x
        if x>=0:
            rev=0
            while x > 0:
                y=x%10
                rev = rev*10+y
                x=x//10
            if rev == copy:
                return True
                
        return False