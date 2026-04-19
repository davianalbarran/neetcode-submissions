class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's algo to detect cycle with discrete steps
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # guaranteed by problem to happen
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow