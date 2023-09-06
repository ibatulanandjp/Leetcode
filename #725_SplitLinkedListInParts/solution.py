# Method: 2 pass method
# 1: Calculate Length
# 2: Split list into k lists
# TC: O(n)
# SC: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []

        # 1: Calculate the length of the linked list
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next

        part_len, rem_len = count // k, count % k
        # 2: Split the list in k parts
        ptr = head
        for i in range(k):
            curr_list = ptr
            if rem_len > 0:
                curr_len = part_len + 1
                rem_len -= 1
            else:
                curr_len = part_len

            if curr_len > 0:
                for j in range(curr_len):
                    temp = ptr
                    if ptr:
                        ptr = ptr.next
                    else:
                        ptr = None

                if temp:
                    temp.next = None
            result.append(curr_list)

        return result
