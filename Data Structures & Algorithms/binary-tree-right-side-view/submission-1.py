# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:        
        res = []
        queue = collections.deque([root])

        while queue:
            rightmost = None
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    rightmost = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightmost:
                res.append(rightmost.val)
        
        return res
            
                    