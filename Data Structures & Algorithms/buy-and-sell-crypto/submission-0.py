class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best_profit = 0

        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                profit = price - cheapest
                if profit > best_profit:
                    best_profit = profit
        return best_profit
        
