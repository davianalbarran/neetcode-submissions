# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, max_val):
            if not curr:
                return 0
            
            max_val = max(max_val, curr.val)
            res = 1 if curr.val >= max_val else 0

            return res + dfs(curr.left, max_val) + dfs(curr.right, max_val)
        
        return dfs(root, root.val)