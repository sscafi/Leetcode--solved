from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        c = 0
        while l1 or l2:
            if not l1:
                a = 0
            else:
                a = l1.val
            if not l2:
                b = 0
            else:
                b = l2.val
            n = a + b + c
            c = 1 if n > 9 else 0
            node = ListNode(n % 10)
            if not head:
                head = node
                temp = node
            else:
                head.next = node
                head = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if c:
            node = ListNode(1)
            head.next = node
        return temp

    def test_addTwoNumbers(self) -> None:
        # Test input linked lists
        l1 = ListNode(3, ListNode(5, ListNode(6)))
        l2 = ListNode(6, ListNode(8, ListNode(9)))

        # Test the addTwoNumbers method
        result = self.addTwoNumbers(l1, l2)

        # Print the result (linked list)
        while result:
            print(result.val, end=" ")
            result = result.next
        print()

# Instantiate the Solution class for testing
test_solution = Solution()
test_solution.test_addTwoNumbers()
