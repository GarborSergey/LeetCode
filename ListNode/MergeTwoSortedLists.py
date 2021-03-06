# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        res = result  # без этого будет выводить только голову, а с этим выводит весь список
        while list1 and list2:
            if list1.val > list2.val:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next

            result = result.next

        if list1:
            result.next = list1
        elif list2:
            result.next = list2
        return res.next