# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        # move right pointer to the node whose next pointer we want to shift
        # if linked list is size 1 and n >= 1, we break out and leave right null
        while n > 0 and right:
            right = right.next
            n -= 1

        # move left to position with right to keep gap consistent
        # move right to null node, leaving left exactly 1 + n away from the null node
        # this will leave left pointing at the correct node whose link should break and go to the following link
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next # once left is in place, replace next node with the proceeding node to remove it

        return dummy.next
        