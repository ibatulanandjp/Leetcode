# Method: Use 2 pointers with a dummy node
# Travel right pointer n steps ahead, then move both pointers until right reaches the end
# TC: O(n), where n is the length of the linked list
# SC: O(1)
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = dummy = ListNode(0, head)
        right = head
        for _ in range(n):
            right = right.next

        # Find the node to remove
        while right:
            left = left.next
            right = right.next
        
        # Remove the left's next node
        left.next = left.next.next
        
        return dummy.next