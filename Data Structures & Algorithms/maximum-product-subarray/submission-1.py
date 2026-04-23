class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # subarray must be a contiguous string of numbers, can't skip
        res = max(nums)
        cur_min = cur_max = 1
        
        for num in nums:
            if num == 0:
                cur_min = cur_max = 1
                continue
            
            tmp = cur_max * num # necessary since we're mutating cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(tmp, num * cur_min, num)

            res = max(res, cur_max)
        
        return res