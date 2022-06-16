from typing import List

class Solution :
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) :
        i, j, k = m-1, n-1, m+n-1

        while i>=0 and j>=0 :
            if nums1[i] > nums2[j] :
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else :
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        
        while j>=0 :
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)

sol = Solution()
sol.mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3)
# sol.mergeSortedArray([0], 0, [1], 1)