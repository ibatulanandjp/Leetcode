from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = self.getListLength(headA)
        lenB = self.getListLength(headB)

        if lenA >= lenB:
            diff = lenA-lenB
            # Move headA ahead by the diff
            for i in range(diff):
                headA = headA.next
        else:
            diff = lenB-lenA
            # Move headB ahead by the diff
            for i in range(diff):
                headB = headB.next

        # Traverse the whole list from there
        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getListLength(self, head: ListNode) -> int:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        return count
