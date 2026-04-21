class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                powerset.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return powerset