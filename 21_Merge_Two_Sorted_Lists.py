# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            prev = ListNode(list1.val, None)
            list1 = list1.next
        else:
            prev = ListNode(list2.val, None)
            list2 = list2.next
        start = prev
        
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val, None)
                list1 = list1.next
            else:
                node = ListNode(list2.val, None)
                list2 = list2.next
            prev.next = node
            prev = prev.next
        
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        
        return start

