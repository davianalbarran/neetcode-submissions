# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        pointer = root

        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            pointer = stack.pop()
            n += 1
            if n == k:
                return pointer.val
            pointer = pointer.right
        return -1
            
            
                
