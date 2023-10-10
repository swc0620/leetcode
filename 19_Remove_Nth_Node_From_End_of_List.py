# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next
        
        prev_prev = None
        prev = head
        while fast:
            fast = fast.next
            prev_prev = prev
            prev = prev.next
        if not prev_prev:
            return prev.next
        prev_prev.next = prev.next
        return head

