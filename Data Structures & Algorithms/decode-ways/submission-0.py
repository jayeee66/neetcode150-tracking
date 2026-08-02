# DP bottom-up
class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [0] * (n + 1)
        # empty string
        dp[0] = 1
        # one char string
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        # two char string or more
        for i in range(2, n+1):
            # choose decode one char and first char is not '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # choose decode two char
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]