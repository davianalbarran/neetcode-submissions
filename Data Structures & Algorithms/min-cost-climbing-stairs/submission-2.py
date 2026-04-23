class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # like most dp problems, there's a brute force solution
        # can't be greedy with a two jump everytime bc we can land on a step that costs a lot more
        # we can eliminate repeated work by starting from the end and memoize repeated work

        for i in range(len(cost) -3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])


        # min_cost = float("inf")
        
        # def step(i, prev_cost):
        #     if i > target_step: # overshot
        #         return
            
        #     if i == target_step: # hit target
        #         min_cost = min(min_cost, jump_cost)
        #         return
            
        #     # if here, still in bounds
        #     jump_cost = cost[i] + prev_cost
            
        #     step(i+1, jump_cost)

        #     step(i+2, jump_cost)

        # step(0, 0)
        # step(1, 0)

        # return min_cost