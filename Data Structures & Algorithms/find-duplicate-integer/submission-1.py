class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force would prob use a set, something like:
        numset = set()

        for num in nums:
            if num in numset:
                return num
            numset.add(num)
        
        return -1
