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
            if carry == 1:
                q, r = divmod(l1.val + l2.val + carry, 10)
            else:
                q, r = divmod(l1.val + l2.val, 10)
            head.next = ListNode(r, None)
            head = head.next
            carry = q
            l1, l2 = l1.next, l2.next
        while l1:
            if carry == 1:
                q, r = divmod(l1.val + carry, 10)
            else:
                q, r = divmod(l1.val, 10)
            head.next = ListNode(r, None)
            head = head.next
            carry = q
            l1 = l1.next
        while l2:
            if carry == 1:
                q, r = divmod(l2.val + carry, 10)
            else:
                q, r = divmod(l2.val, 10)
            head.next = ListNode(r, None)
            head = head.next
            carry = q
            l2 = l2.next
        if carry:
            head.next = ListNode(carry, None)

        return dummy.next
