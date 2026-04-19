class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stack_val, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx)
            stack.append([val, i])
        
        return res