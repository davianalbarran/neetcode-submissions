# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use combo of merge sort and merging two sorted linked lists
        # for latter, see sol'n @ https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150$0
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []

            # iterate through two lists at a time so we can merge them with helper function
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.mergeLists(list1, list2))
            lists = merged
        
        return lists[0]

    def mergeLists(self, list1, list2):
        starter_node = ListNode()
        tail = starter_node

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # only one of the below can be true since we broke out of above while loop for one of them
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return starter_node.next