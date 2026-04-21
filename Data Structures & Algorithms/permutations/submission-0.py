class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # there are n! permutations so that is the limit of performance
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:]) # recursively iterate through smaller and smaller list
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res


        # def dfs(i, cur):
        #     if not cur or i >= len(nums):
        #         return
            
        #     if len(cur) == len(nums):
        #         res.append(cur.copy())
        #         return
            
            

        #     cur.append(nums[i])
