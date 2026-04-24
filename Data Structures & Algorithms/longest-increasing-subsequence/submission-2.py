class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # this solution works because it retains the last_num we iterated through
        # for ALL subpaths. Yes it's O(n^2) but the constraints are not very large
        # There IS a faster solution using patience sorting which I just learned about
        # see sol'n 3 for that
        dp = [1] * len(nums) # e.g. len = 7 -> [1,1,1,1,1,1,1]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)