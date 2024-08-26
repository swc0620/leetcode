class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(idx, is_turn_to_buy):
            if idx >= len(prices):
                return 0
            if (idx, is_turn_to_buy) in dp:
                return dp[(idx, is_turn_to_buy)]
            
            cooldown = dfs(idx+1, is_turn_to_buy)
            if is_turn_to_buy:
                buy = dfs(idx+1, not is_turn_to_buy) - prices[idx]
                dp[(idx, is_turn_to_buy)] = max(buy, cooldown)
            else:
                sell = dfs(idx+2, not is_turn_to_buy) + prices[idx]
                dp[(idx, is_turn_to_buy)] = max(sell, cooldown)
            return dp[(idx, is_turn_to_buy)]
        
        return dfs(0, True)