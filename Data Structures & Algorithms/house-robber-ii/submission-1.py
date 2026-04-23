class Solution:
    def rob(self, nums: List[int]) -> int:
        # we need to run house robber I function on either the array of all
        # elements starting at 0 and not including the last OR the array
        # of all elements starting at 1
        if len(nums) == 1:
            return nums[0]

        return max(self.classic_rob(nums[0:len(nums)-1]), self.classic_rob(nums[1:]))

    def classic_rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2 # exactly the same as house robber I