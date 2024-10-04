# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        carry = 0
        while l1 and l2:
            carry, r = divmod(l1.val + l2.val + carry, 10)
            head.next = ListNode(r, None)
            head = head.next
            l1, l2 = l1.next, l2.next
        while l1:
            carry, r = divmod(l1.val + carry, 10)
            head.next = ListNode(r, None)
            head = head.next
            l1 = l1.next
        while l2:
            carry, r = divmod(l2.val + carry, 10)
            head.next = ListNode(r, None)
            head = head.next
            l2 = l2.next
        if carry:
            head.next = ListNode(carry, None)

        return dummy.next