"""LeetCode 235: Lowest Common Ancestor of a Binary Search Tree.

Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Time complexity: O(h), where h is the tree height.
Auxiliary space complexity: O(1).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        current = root
        while current:
            if (current.val - p.val) * (current.val - q.val) <= 0:
                return current
            else:
                if current.val < p.val and current.val < q.val:
                    current = current.right
                else:
                    current = current.left
