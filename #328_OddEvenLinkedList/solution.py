from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        evenStart = even

        while even != None and even.next != None:

            # Process odd nodes
            odd.next = even.next
            odd = odd.next

            # Process even nodes
            even.next = odd.next
            even = even.next

            # if odd:
            #     print("Odd", odd.val)
            # if even:
            #     print("Even", even.val)

        odd.next = evenStart

        return head
