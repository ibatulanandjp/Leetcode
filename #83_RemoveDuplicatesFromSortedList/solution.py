from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n1.next = n2
n2.next = n3

sol = Solution()
res = sol.deleteDuplicates(n1)
while res:
    print(res.val)
    res = res.next