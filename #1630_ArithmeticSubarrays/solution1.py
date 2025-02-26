# Method: For each subarray, sort and check
# TC: O(m * n * logn)
# SC: O(n)
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True

        
        res = []
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            res.append(check(arr))

        return res