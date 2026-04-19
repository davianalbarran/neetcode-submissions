# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f_num = 0
        s_num = 0

        tracker = 1
        while l1:
            num_to_add = l1.val * tracker
            f_num += num_to_add
            tracker *= 10
            l1 = l1.next
        
        tracker = 1
        while l2:
            num_to_add = l2.val * tracker
            s_num += num_to_add
            tracker *= 10
            l2 = l2.next
        
        res_sum = f_num + s_num

        array_nodes = []
        res = ListNode()

        while True:
            rightmost_digit = res_sum % 10
            node = ListNode(rightmost_digit)
            array_nodes.append(node)
            res_sum //= 10
            if res_sum == 0:
                break
        
        res.next = array_nodes[0] if len(array_nodes) > 0 else None
        head = res
        
        for i, node in enumerate(array_nodes):
            node.next = array_nodes[i + 1] if (i + 1) < len(array_nodes) else None
        
        return head.next
