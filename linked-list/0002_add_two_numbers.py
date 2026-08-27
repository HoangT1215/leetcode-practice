"""LeetCode 2: Add Two Numbers.

Problem: https://leetcode.com/problems/add-two-numbers/

Time complexity: O(max(m, n))
Auxiliary space complexity: O(1), excluding the returned list

LeetCode provides the ListNode class; do not redefine it in the submission.
"""

from typing import Optional


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                digit1 = l1.val
            else:
                digit1 = 0

            if l2:
                digit2 = l2.val
            else:
                digit2 = 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
