class Solution:
    # patience sorting method: O(nlogn) because we're running 
    # binary search n times.
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []  # tops of each pile
        for num in nums:
            # Binary search to find leftmost pile with top >= num
            left, right = 0, len(piles)
            while left < right:
                mid = (left + right) // 2
                if piles[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            # If found, replace; otherwise append
            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num
        return len(piles)