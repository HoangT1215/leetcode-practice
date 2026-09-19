"""LeetCode 15: 3Sum.

Problem: https://leetcode.com/problems/3sum/

Time complexity: O(n^2)
Space complexity: O(1), excluding the output and sorting implementation.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate left values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return output
