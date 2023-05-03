from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Return if only 1 or 2 elements in the list
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        # Keep a pointer at the start of even, for adding it to the end of oddList
        evenStart = even

        while odd.next != None and even.next != None:
            # Process odd nodes
            odd.next = even.next
            odd = odd.next

            # Process even nodes
            even.next = odd.next
            even = even.next

        odd.next = evenStart

        return head
