'''
Recursive solution to reverse a liked list
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head, None)

    def _reverse(self, head, prev):
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self._reverse(temp, prev)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

sol = Solution()
res = sol.reverseList(n1)
while res:
    print(res.val)
    res = res.next