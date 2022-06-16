from typing import List

class Solution :
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) :

        for i in range(len(nums1)) :
            if i > m-1 :
                nums1[i] += nums2[i-m]

        nums1.sort()
        print(nums1)

sol = Solution()
sol.mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3)
# sol.mergeSortedArray([0], 0, [1], 1)