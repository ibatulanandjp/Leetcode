'''
[Method]: Flattening of matrix into a list, and then reshaping the matrix
'''

from typing import List


class Solution:
    def reshapeTheMatrix(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        # Return the original matrix if size is different
        if r*c != len(mat)*len(mat[0]):
            return mat

        # Flatten the matrix into a list
        nums = sum(mat, [])

        # Create the reshaped matrix
        res: List[List[int]] = []
        l: int = 0

        # Append all the elements from the list into the new matrix row-by-row
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[l])
                l += 1
            res.append(temp)

        return res


sol = Solution()
print(sol.reshapeTheMatrix([[1, 2], [3, 4]], 1, 4))
# print(sol.reshapeTheMatrix([[1, 2], [3, 4]], 4, 1))
