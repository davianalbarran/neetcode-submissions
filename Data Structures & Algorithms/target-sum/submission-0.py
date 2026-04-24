class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we can use backtracking to go through every possible combination of
        # adding and subtracting nums
        # not efficient enough for the problem constraints though, O(2^n)
        
        # let's add memoization to it
        dp = {}

        def backtrack(i, cur_sum):
            # without this below check, the function still technically works
            # if we return rather than store that result at the end in dp,
            # it's just too slow
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            dp[(i, cur_sum)] = (
                backtrack(i + 1, cur_sum + nums[i]) + # path if we add
                backtrack(i + 1, cur_sum - nums[i])   # path if we subtract
            )
            return dp[(i, cur_sum)]
        
        return backtrack(0, 0)