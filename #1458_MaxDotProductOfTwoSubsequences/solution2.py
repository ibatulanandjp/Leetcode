# Method: Use Optimized Dynamic Programming (1D) with 2 arrays of current and previous.
# Since, wee only need values from the current and previous row to compute the next row
# We swap the two arrays, thus making the current array act as the previous array for the next iteration.
# TC: O(n * m)
# SC: O(n)
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        current = [float('-inf')] * (m + 1)
        previous = [float('-inf')] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_prod = nums1[i-1] * nums2[j-1]
                current[j] = max(curr_prod, previous[j],
                                 current[j-1], curr_prod + max(0, previous[j-1]))
            current, previous = previous, current

        return previous[m]
