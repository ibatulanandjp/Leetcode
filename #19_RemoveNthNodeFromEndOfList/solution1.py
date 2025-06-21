from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        todel = ahead = head
        for i in range(n):
            ahead = ahead.next

        if not ahead:
            return head.next

        while ahead.next:
            todel = todel.next
            ahead = ahead.next

        todel.next = todel.next.next
        return head
