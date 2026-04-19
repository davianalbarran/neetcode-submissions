# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # pretty quick solution but faster than O(n) possible with Floyd's Tortoise and Hare
        # node_set = {head}

        # while head:
        #     head = head.next
        #     if head in node_set:
        #         return True
        #     node_set.add(head)
        
        # return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

            if fast.next:
                fast = fast.next
            else:
                return False

            if slow == fast:
                return True
        
        return False