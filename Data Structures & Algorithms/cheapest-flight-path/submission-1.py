# Bellman-Ford algo - good here for the at most k constraint

# Start at source node, then do BFS

# For each level traversed, keep track of min cost

# We want the initial costs to other nodes to be infinity

# When we reach a node that cost less to traverse to, we will update a temporary array rather than
# the original

# Using a temp array allows us to retain the integrity of the original array so we don't accidentally
# skip edges because we previously traversed the path and assigned the minimum we saw on that path to
# the original

# We use Bellman-Ford because it's much simpler to implement in this prob and maintains the Big O
# Complexity O(E * k)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        N = len(flights)
        prices = [float("infinity")] * n
        prices[src] = 0

        for i in range(k + 1): # specific to this prob - k stops means we can move k + 1 levels
            tmp_prices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"): # can't reach this node if price is infinity
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p # save the smaller price
            
            # now we can persist prices since we went through all the flights
            # if the iteration through our flights returns something smaller
            prices = tmp_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1