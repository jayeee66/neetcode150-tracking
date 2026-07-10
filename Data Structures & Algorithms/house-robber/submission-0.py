class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        dp[0] = nums[0]
        if n == 0:
            return 0
        if n == 1:
            return dp[0]
        # 
        dp[1] = max(dp[0], nums[1])
        # choose not to steal, if it's less than previous
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]
        