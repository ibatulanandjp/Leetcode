from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = currentHead = ListNode()

        # Compare and add the smaller node to the list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        # Add the remaining nodes from either of the lists to the current list
        if list1 or list2:
            current.next = list1 if list1 else list2

        return currentHead.next


# Create 1st linked list with values
n11 = ListNode(1)
n12 = ListNode(2)
n13 = ListNode(4)

n11.next = n12
n12.next = n13

# print("---List1---")
# list1.printList()


# Create 2nd linked list with values
n21 = ListNode(1)
n22 = ListNode(3)
n23 = ListNode(4)

n21.next = n22
n22.next = n23

# print("---List2---")
# list2.printList()



sol = Solution()
res = sol.mergeTwoLists(n11, n21)
print("---Merged List---")
while res.next is not None:
    print(res.val)
    res = res.next
