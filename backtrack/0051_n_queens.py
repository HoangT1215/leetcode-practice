"""LeetCode 51: N-Queens.

Problem: https://leetcode.com/problems/n-queens/

Time complexity: O(n!)
Space complexity: O(n^2), including the board
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        if n == 1:
            return [["Q"]]
        else:
            # Incorrect attempt: this did not account for the possibility that
            # no valid solution exists for a branch.
            # for i in range(n):
            #     first_row = "." * i + "Q" + "." * (n - i - 1)
            #     for config in self.solveNQueens(n - 1):
            #         solution = [first_row]
            #         for row in config:
            #             solution.append(row[:i] + "." + row[i:])
            #         output.append(solution)

            cols = set()
            diagonals = set()       # row - col
            anti_diagonals = set()  # row + col
            board = [["."] * n for _ in range(n)]

            def backtrack(row: int) -> None:
                if row == n:
                    # Best way:
                    # solution = ["".join(board_row) for board_row in board]

                    # Another implementation:
                    solution = []
                    for board_row in board:
                        final_row = ""
                        for cell in board_row:
                            final_row += cell
                        solution.append(final_row)

                    output.append(solution)
                    return
                else:
                    for col in range(n):
                        if (
                            col in cols
                            or row - col in diagonals
                            or row + col in anti_diagonals
                        ):
                            continue
                        else:
                            board[row][col] = "Q"
                            cols.add(col)
                            diagonals.add(row - col)
                            anti_diagonals.add(row + col)

                            # Move to the next row. If no column works there,
                            # the call finishes and we return to try a new
                            # placement in this row.
                            backtrack(row + 1)

                            # Undo the placement.
                            board[row][col] = "."
                            cols.remove(col)
                            diagonals.remove(row - col)
                            anti_diagonals.remove(row + col)

            # The initial row is 0; the terminating row is n.
            backtrack(0)

        return output
