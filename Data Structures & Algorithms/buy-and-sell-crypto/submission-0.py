class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > biggest_profit:
                    biggest_profit = profit
        return biggest_profit