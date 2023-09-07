# Method: Find the left position and reverse the sublist in between, keeping the left end intact
# TC: O(n)
# SC: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        curr = dummy.next

        # Find the left position
        for _ in range(1, left):
            curr = curr.next
            pre = pre.next

        # Reverse the sublist in between
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next

            pre.next = temp

        return dummy.next
