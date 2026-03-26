#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1959992333/
# Language: python3
# Date: 2026-03-26


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left,right = 0,1
        # max_profit = 0
        # while left < len(prices):
        #     if right < len(prices):
        #         if prices[left] < prices[right]:
        #             profit = prices[right] - prices[left]
        #             if profit > max_profit:
        #                 max_profit = profit
        #         right += 1
        #     else:
        #         left += 1
        #         right = left + 1
        # return max_profit

        stack = []
        profit = 0
        for i, p in enumerate(prices):
            if stack and stack[-1] < p:
                profit = max(p-stack[-1],profit)
            else:
                stack.append(p) 
        return profit







        # daily_prices = {}
        # profit = 0
        # list_len = len(prices)

        # for day in range(list_len):
        #     daily_prices[day] = prices[day+1:]
        #     if day==(list_len-1):
        #         daily_prices[day] = [prices[list_len-1]]

        # for price in daily_prices:
        #     sell_stock = max(daily_prices[price])
        #     _profit = sell_stock - prices[price]
        #     if _profit > profit:
        #         profit = _profit

        # return profit

        
