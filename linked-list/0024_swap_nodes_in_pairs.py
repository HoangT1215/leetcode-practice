from __future__ import annotations


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        previous = dummy

        # Iterate only when a complete pair exists.
        while previous.next and previous.next.next:
            # previous -> first -> second -> rest
            first = previous.next
            second = first.next
            rest = second.next

            # previous -> second -> first -> rest
            previous.next = second
            second.next = first
            first.next = rest

            # `first` is now the last node of the swapped pair.
            previous = first

        return dummy.next
