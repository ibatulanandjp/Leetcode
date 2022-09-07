from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # If head exist
        if head:
            prev = head
            temp = head.next
        # Empty List
        else:
            return None

        # Remove elements from the beginning
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None

        # Remove elements in the middle and end 
        while temp:
            # print(temp.val)
            if temp.val == val:
                temp = temp.next
                prev.next = temp
            else:
                prev = temp
                temp = temp.next

        return head


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