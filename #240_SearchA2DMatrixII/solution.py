from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            if target >= matrix[r][0] and target <= matrix[r][col-1]:
                res = self.binarySearch(matrix[r], target)
                if res:
                    return True
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return True
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        return False
