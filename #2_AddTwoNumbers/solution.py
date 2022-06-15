from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%d" % self.val


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumList: Optional[ListNode] = ListNode(0, None)
        carry = 0

        ptr1 = l1
        ptr2 = l2
        sumPtr = sumList

        while ptr1 != None or ptr2 != None:

            x = ptr1.val if ptr1 != None else 0
            y = ptr2.val if ptr2 != None else 0

            sum = x + y + carry
            carry = sum//10

            sumPtr.next = ListNode(sum % 10, None)
            sumPtr = sumPtr.next

            if ptr1 != None:
                ptr1 = ptr1.next
            if ptr2 != None:
                ptr2 = ptr2.next

        if carry > 0:
            sumPtr.next = ListNode(carry, None)

        return sumList.next


sol = Solution()

l13 = ListNode(3, None)
l12 = ListNode(4, l13)
l11 = ListNode(2, l12)

l23 = ListNode(4, None)
l22 = ListNode(6, l23)
l21 = ListNode(5, l22)

res = sol.addTwoNumbers(l11, l21)
resPtr = res
while resPtr != None:
    print(resPtr.val, end=" ")
    resPtr = resPtr.next
