"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_node_to_copy_node_map = { None: None } # null nodes should map to null nodes

        cur = head
        while cur:
            copy = Node(cur.val)
            old_node_to_copy_node_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_node_to_copy_node_map[cur] # returns the copy we made in the previous loop
            copy.next = old_node_to_copy_node_map[cur.next] # returns the copy of node that the old node pointed to
            copy.random = old_node_to_copy_node_map[cur.random] # returns the copy of the node that the old node's random pointer pointed to
            cur = cur.next

        return old_node_to_copy_node_map[head] # returns the copy of the old head node we made in the first loop

        