from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row_id, row in enumerate(matrix):

            if target >= row[0] or target <= row[-1]:
                for col_id, element in enumerate(row):
                    if element == target:
                        return True
                    elif element > target:
                        return False


sol = Solution()
# res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
print(res)
