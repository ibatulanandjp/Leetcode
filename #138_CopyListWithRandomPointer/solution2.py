# Method: Interleaving lists in 3 steps
# 1: Add copy node in the list (After original node)
# 2: Shift random pointer
# 3: Separate original and copy lists
# TC: O(1)
# TC: O(1)
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Add copy node in the list
        ptr = head
        while ptr:
            node = Node(ptr.val, ptr.next)
            ptr.next = node
            ptr = node.next

        # Shift random pointer
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        # Separate original and copy lists
        original_head = head
        copy_head = head.next
        ptr = original_head
        copy = copy_head
        while ptr:
            ptr.next = ptr.next.next
            copy.next = copy.next.next if copy.next else None
            ptr = ptr.next
            copy = copy.next

        return copy_head
