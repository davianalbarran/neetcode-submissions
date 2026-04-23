class Solution:
    def rob(self, nums: List[int]) -> int:
        # there's a decision tree here that makes you realize there's a clear subproblem
        # if you rob i=0, then you need to compute how much the subarray after i=1 is worth
        # if you rob i=1, then you need to compute how much the subarray after i=2 is worth
        # the pattern is choosing to rob a house "n" means you will need add the value of the
        # houses starting at index (n + 2)
        rob1 = rob2 = 0 # rob2 is the house we just robbed and rob1 will be the house just before that

        for n in nums:
            # the below max call will be the decider in whether we rob n or stick with the previous house
            temp = max(n + rob1, rob2) # store the max that rob2 will hold after robbing this house
            rob1 = rob2 # set rob1 equal to rob2 since it's now the previous house
            rob2 = temp # now update rob2 to our current max value
        
        return rob2 # rob2 will hold the largest sum we can rob