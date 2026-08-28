"""LeetCode 465: Optimal Account Balancing.

Problem: https://leetcode.com/problems/optimal-account-balancing/

Time complexity: O(m!) in the worst case, where m is the number of
nonzero net balances
Space complexity: O(m)
"""

from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = {}

        for sender, receiver, amount in transactions:
            balance[sender] = balance.get(sender, 0) - amount
            balance[receiver] = balance.get(receiver, 0) + amount

        # Only record accounts with nonzero debt; no need to keep track of
        # the original transaction graph after computing net balances.
        debt = [
            amount
            for amount in balance.values()
            if amount != 0
        ]

        # We now have a zero-sum list of nonzero accounts. Find the minimum
        # number of actions required to clear them all.
        def backtrack(start: int) -> int:
            while start < len(debt) and debt[start] == 0:
                start += 1

            if start == len(debt):
                return 0

            best = float("inf")
            seen = set()

            for j in range(start + 1, len(debt)):
                # A transaction can only settle opposite-sign balances.
                if debt[start] * debt[j] >= 0:
                    continue

                # Equal balances produce equivalent search branches.
                if debt[j] in seen:
                    continue
                seen.add(debt[j])

                original = debt[j]

                # Treat debt[start] as settled. Account j absorbs the
                # remaining balance, and the recursion moves past start.
                debt[j] += debt[start]
                best = min(best, 1 + backtrack(start + 1))

                # Undo the choice before trying another account.
                debt[j] = original

                # Exact cancellation clears two accounts, which is the best
                # possible result for this step.
                if original + debt[start] == 0:
                    break

            return best

        return backtrack(0)
