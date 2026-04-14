# Two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0(buy)
        r = 1(sell)
        max_profit = 0
        while r < len(prices):
            # If buy is larger than sell, the sell day is a better buy day
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            r += 1
        return max_profit
