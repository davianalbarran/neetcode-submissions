class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        # max_area = -1
        # l = 0

        # while l <= len(heights) - 2:
        #     r = len(heights) - 1
        #     while r > l:
        #         temp = min(heights[l], heights[r]) * abs(l - r)

        #         if (temp > max_area):
        #             max_area = temp
                
        #         print(f"l: {l}, r: {r}, temp: {temp}, max_area: {max_area}")
        #         r-=1
            
        #     l+=1
        
        # return max_area