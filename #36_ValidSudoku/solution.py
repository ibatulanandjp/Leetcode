from calendar import c
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Create 9 sets for each element in the rows, columns, and sub-boxes
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxes = [set() for x in range(9)]

        for row_id, row in enumerate(board):
            for col_id, element in enumerate(row):

                # If "." found, skip it
                if element == ".":
                    continue

                # Calculate the box id (0-9)
                box_id = (row_id // 3) * 3 + (col_id // 3)

                # If the current element exist in the either of the set of row, col, or box, then return False
                if element in rows[row_id] or element in cols[col_id] or element in boxes[box_id]:
                    return False

                # Add the current element to the sets
                rows[row_id].add(element)
                cols[col_id].add(element)
                boxes[box_id].add(element)

        # If all the sets are okay, return True
        return True


sol = Solution()
res = sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
                        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

# res = sol.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
#                         "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

print(res)
