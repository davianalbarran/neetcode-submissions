# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(curr):
            if not curr:
                return 0
            
            left_max = dfs(curr.left)
            right_max = dfs(curr.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            self.res = max(self.res, curr.val + left_max + right_max)

            return curr.val + max(left_max, right_max)
        
        dfs(root)
        return self.res