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
        hashmap = {None: None}
        node = head
        while node:
            new_node = Node(node.val, None, None)
            hashmap[node] = new_node
            node = node.next

        node = head
        while node:
            copy = hashmap[node]
            copy.next = hashmap[node.next]
            copy.random = hashmap[node.random]
            node = node.next

        return hashmap[head]
        