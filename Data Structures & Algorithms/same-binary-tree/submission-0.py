# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
        # queue = collections.deque([p, q])

        # while queue:
        #     for i in range(len(queue)):
        #         left = queue.popleft() if queue else None
        #         right = queue.pop() if queue else None

        #         if left.val != right.val:
        #             return False
                
        #         queue.extend([left.left, left.right, right.left, right.right])
        
        # return True
