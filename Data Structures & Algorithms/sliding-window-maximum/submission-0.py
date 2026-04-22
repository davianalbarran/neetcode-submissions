class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue_idxs = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while queue_idxs and nums[queue_idxs[-1]] < nums[r]:
                queue_idxs.pop()

            queue_idxs.append(r)

            if l > queue_idxs[0]:
                queue_idxs.popleft()
            
            if (r + 1) >= k:
                res.append(nums[queue_idxs[0]])
                l += 1
            
            r += 1

        return res

        