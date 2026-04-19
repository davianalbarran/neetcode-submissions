class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        l = 0

        while l <= len(heights) - 2:
            r = len(heights) - 1
            while r > l:
                temp = min(heights[l], heights[r]) * abs(l - r)

                if (temp > max_area):
                    max_area = temp
                
                print(f"l: {l}, r: {r}, temp: {temp}, max_area: {max_area}")
                r-=1
            
            l+=1
        
        return max_area
        # firstMax = (-1, -1)
        # secondMax = (-1, -1)

        # for i, a in enumerate(heights):
        #     if a > firstMax[0]:
        #         secondMax = firstMax
        #         firstMax = (a, i)
        #     elif a > secondMax[0]:
        #         secondMax = (a, i)

        #     print(f"i: {i}, a: {a}, first: {firstMax}, second: {secondMax}")
        
        # return secondMax[0] * abs(firstMax[1] - secondMax[1])