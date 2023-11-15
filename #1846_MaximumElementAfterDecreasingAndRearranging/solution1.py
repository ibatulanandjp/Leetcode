# Method: Greedy approach - Sort and count the subsequent number if it is greater by 1
# TC: O(n logn), for sorting the number
# SC: O(n), for sorting (Tim sort)
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1

        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1
        return ans
