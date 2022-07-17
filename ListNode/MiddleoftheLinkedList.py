# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

x = ListNode(3)
n = ListNode(10, x)
print(n.next.val)

print()

class Solution:
    def middleNode(self, head):
        result = []
        while head:
            result.append(head)
            head = head.next

        return (result[(len(result) // 2)])