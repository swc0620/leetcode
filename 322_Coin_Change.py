class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for c in coins:
            if c < amount:
                dp[c] = 1

        for n in range(1, amount+1):
            for c in coins:
                if n - c >= 0:
                    dp[n] = min(dp[n], dp[n-c] + 1)
        
        if dp[amount] == (amount+1):
            return -1
        return dp[amount]