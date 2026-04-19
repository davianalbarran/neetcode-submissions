class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        rec_idx_height_stack = []

        for i, h in enumerate(heights):
            start = i
            while rec_idx_height_stack and rec_idx_height_stack[-1][1] > h:
                idx, height = rec_idx_height_stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            
            rec_idx_height_stack.append((start, h))
        
        for idx, height in rec_idx_height_stack:
            max_area = max(max_area, height * (len(heights) - idx))
        
        return max_area
        