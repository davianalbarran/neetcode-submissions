class Solution:
    def climbStairs(self, n: int) -> int:
        # we know that the last two steps in the sequence will be 1
        # step n - 1 will always be reached by one step
        # step n can be set to one as well
        one, two = 1, 1

        # every proceeding step will be the sum of the last two
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

            