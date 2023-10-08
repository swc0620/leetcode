# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        front, back = head, head
        while front and back:
            if not back.next or not front.next or not front.next.next:
                return False
            back = back.next
            front = front.next.next
            if front == back:
                return True
        
        return False