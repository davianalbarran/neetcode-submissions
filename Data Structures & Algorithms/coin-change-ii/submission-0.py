class Solution:
    # 2D dp sol'n - looks closest to coin change I except with 2d cache
    # to reduce memory complexity, we can flip the loops to iterate coins first then amount
    # this will allow us to reduce our cache to just store one row rather than all rows
    # we'd store next dp cache, run through the amount loop, then set the orig cache to the next cache
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1] # skip the coin by default

                if a - coins[i] >= 0: # if this is a valid path
                    dp[a][i] += dp[a - coins[i]][i] # choose the coin and move on
        
        return dp[amount][0]