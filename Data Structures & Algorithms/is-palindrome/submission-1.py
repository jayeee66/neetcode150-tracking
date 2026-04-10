# Reverse string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''
        e = ''
        for i in range(len(s)):
            if s[i].isalnum():
                f += s[i].lower()
        print(f)
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                e += s[i].lower()
        print(e)
        return f == e