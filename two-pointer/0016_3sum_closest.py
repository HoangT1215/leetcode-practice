"""LeetCode 16: 3Sum Closest.

Problem: https://leetcode.com/problems/3sum-closest/

Time complexity: O(n^2)
Space complexity: O(1), excluding the sorting implementation.
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if (total - target) ** 2 < (closest - target) ** 2:
                    closest = total

                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return target

        return closest
