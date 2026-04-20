# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def valid(node, bound_low, bound_high):
            if not node:
                return True
            if not (node.val < bound_high and node.val > bound_low):
                return False
            
            return (valid(node.left, bound_low, node.val)
                    and valid(node.right, node.val, bound_high))
        
        return valid(root, float("-infinity"), float("infinity"))