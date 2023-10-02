class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price = prices[0], prices[0]
        res = 0
        for price in prices:
            max_price = max(max_price, price)
            res = max(res, max_price - min_price)
            if price < min_price:
                res = max(res, max_price - min_price)
                min_price = price
                max_price = price
        
        return res
