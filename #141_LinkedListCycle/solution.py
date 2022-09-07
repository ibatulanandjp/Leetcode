from operator import ne
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

sol = Solution()
res = sol.hasCycle(n1)
print(res)