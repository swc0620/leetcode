class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount+1)] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        
        if dp[amount] == (amount+1):
            return -1
        return dp[amount]