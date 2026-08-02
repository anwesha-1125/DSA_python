class Solution:
    def pallindrome(self ,i, s)->bool:
        if i == len(s)//2:
            return True
        if s[i] != s[len(s) - i - 1]:
            return False
        return self.pallindrome(i+1,s)

    def isPalindrome(self, s: str) -> bool:
        new = ""
        #Ignore spaces.
        #Ignore punctuation (,, :, etc.).
        #Ignore uppercase/lowercase differences.
        for ch in s.lower():
            if ch.isalnum():
                new += ch
        return self.pallindrome(0, new)