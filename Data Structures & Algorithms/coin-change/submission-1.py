class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unbounded knapsack dp problem
        # dp problems we typically want to work from the "bottom up"
        # in this case, instead of trying to bring 7 down to 0, let's
        # start from 0 and try to get to 7
        # this way we can cache our work getting there and we will reveal the
        # optimal path by choosing the path that gets us there quickest

        dp = [amount + 1] * (amount + 1) # basically fill an array with the upper bound of largest values
        dp[0] = 0 # it takes 0 coins to get to 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0: # if we have a possible path with this coin
                    dp[a] = min(dp[a], 1 + dp[a - c]) # cache the smaller between 
        
        return dp[amount] if dp[amount] != amount + 1 else -1