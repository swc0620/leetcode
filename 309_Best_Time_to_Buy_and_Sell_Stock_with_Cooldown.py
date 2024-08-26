class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, turn_to_buy):
            if i >= len(prices):
                return 0
            if (i, turn_to_buy) in dp:
                return dp[(i, turn_to_buy)]
            
            cooldown = dfs(i+1, turn_to_buy)
            if turn_to_buy:
                buy = dfs(i+1, not turn_to_buy) - prices[i]
                dp[(i, turn_to_buy)] = max(cooldown, buy)
            else:
                sell = dfs(i+2, not turn_to_buy) + prices[i]
                dp[(i, turn_to_buy)] = max(cooldown, sell)
            return dp[(i, turn_to_buy)]
        
        return dfs(0, True)
            
