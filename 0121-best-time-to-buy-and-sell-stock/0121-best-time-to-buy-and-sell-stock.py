class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n  = len(prices)
        result = 0
        second_result = float("inf")
        for i in range(0,n):
            if prices[i] < second_result:
                second_result = prices[i]
            current_profit = prices[i] - second_result
            if current_profit > result:
                result = current_profit 

        return result

        