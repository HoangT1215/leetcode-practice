"""LeetCode 55: Jump Game.

Problem: https://leetcode.com/problems/jump-game/

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        else:
            # O(nk) dynamic-programming approach, where k = max(nums).
            # dp = [0] * n
            # dp[0] = 1
            # for i in range(n - 1):
            #     if dp[i] == 1:
            #         for j in range(min(nums[i] + 1, n - i)):
            #             dp[i + j] = 1
            # if dp[n - 1] == 1:
            #     return True
            # else:
            #     return False

            # O(n log n) approach: sort and merge reachable intervals.
            # intervals = []
            # for i in range(n - 1):
            #     intervals.append([i, i + nums[i]])
            # intervals.sort()
            # final_list = intervals[0]
            # for start, end in intervals[1:]:
            #     previous_end = final_list[1]
            #     if start <= previous_end:
            #         final_list[1] = max(previous_end, end)
            #     else:
            #         break
            #
            # final_start, final_end = final_list[0], final_list[1]
            # if final_start == 0 and final_end >= n - 1:
            #     return True
            # else:
            #     return False

            # O(n) greedy approach: farthest is the greatest index reachable
            # using the portion of the array processed so far.
            farthest = 0

            for i in range(n - 1):
                # If i is beyond the reachable prefix, no later index can be
                # used to extend the range.
                if i > farthest:
                    return False

                farthest = max(farthest, i + nums[i])

                if farthest >= n - 1:
                    return True

            return farthest >= n - 1
