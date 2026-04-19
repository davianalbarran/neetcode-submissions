class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if target == curSum:
                return [l+1, r+1]
            elif target < curSum:
                r -= 1
            elif target > curSum:
                l += 1
        
        return []
            
