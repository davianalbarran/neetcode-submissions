class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force would just sort the list in desc order and get the (k-1)th index of the list
        # nums.sort()
        # nums.reverse()
        # return nums[k-1]
        
        # don't need sorting if using max heap
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0

        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        
        return res * -1
