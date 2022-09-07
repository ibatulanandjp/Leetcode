from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # Create a dummy head node in the beginning
        dummy_head = ListNode(-1)
        dummy_head.next = head

        temp = dummy_head
        # Remove elements from the list
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        # Return the list after the dummy_head node
        return dummy_head.next


n1 = ListNode(6)
n2 = ListNode(6)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

sol = Solution()
res = sol.removeElements(n1, 6)
while res:
    print(res.val)
    res = res.next