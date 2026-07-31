# Dynamic Programming 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, maxLen = 0, 1 
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j: # length 1
                    dp[i][j] = True
                elif j == (i + 1): # length 2
                    dp[i][j] = (s[i] == s[j]) # ex. 'aa' 'bb'
                else: # length >= 3
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

                if dp[i][j] and (j - i + 1) > maxLen:
                    start = i
                    maxLen = j - i + 1

        return s[start:start + maxLen]