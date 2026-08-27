"""LeetCode 2880: Select Data.

Problem: https://leetcode.com/problems/select-data/

Time complexity: O(n)
Space complexity: O(m), where m is the number of selected rows
"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]
