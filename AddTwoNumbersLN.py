# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        while l1.next != None:
            n1 += str(l1.val)
            l1 = l1.next
        n1 += str(l1.val)

        n2 = ''
        while l2.next != None:
            n2 += str(l2.val)
            l2 = l2.next
        n2 += str(l2.val)

        result = [int(i) for i in str(int(n1[::-1]) + int(n2[::-1]))]

        node = None

        for i in result:
            node = ListNode(i, node)

        return node