class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force would just sort the list and get the (k-1)th index of the list
        nums.sort()
        nums.reverse()
        return nums[k-1]