# Method: Use a dummy node for result head and iterate through both lists
# taking the smaller node each time.
# TC: O(n + m) where n and m are the lengths of the two lists
# SC: O(1) for the result list, O(n + m) for the input lists if we consider the input as part of the space complexity
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummy.next