class Solution:
    # with brute force recursion -> O(2^n) since we have at most two decisions and the tree height will be n
    # luckily we can cache the boolean buy/sell flag and index
    # this means we'll have n indexes and only two possible states for buy or sell
    # this reduces the complexity to O(n * 2) AKA O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # if we buy -> go to the next day
        # if we sell -> skip a day
        # we can only buy one coin so there is no way to have buy again the next day
        dp = {}

        def dfs(i, didBuy):
            if i >= len(prices):
                return 0

            if (i, didBuy) in dp:
                return dp[(i, didBuy)] # skip computation with caching
            
            cooldown = dfs(i + 1, didBuy) # we can always choose to cooldown

            # our decision splits if we buy or sell
            if didBuy:
                buy = dfs(i + 1, not didBuy) - prices[i] # we either buy, subtracting our profit
                dp[(i, didBuy)] = max(buy, cooldown) # save the max profit we have at this index
            else:
                sell = dfs(i + 2, not didBuy) + prices[i] # or we sell, adding to our profit (hopefully)
                dp[(i, didBuy)] = max(sell, cooldown)
            
            return dp[(i, didBuy)]
        
        return dfs(0, True)