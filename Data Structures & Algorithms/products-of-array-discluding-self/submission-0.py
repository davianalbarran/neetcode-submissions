class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]

            result.append(math.prod(left + right))

        return result