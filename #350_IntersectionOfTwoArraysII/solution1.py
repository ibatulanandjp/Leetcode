from typing import List

class Solution :
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int] :
        res: List[int] = []

        map1 = {}
        map2 = {}

        for i, val in enumerate(nums1) :
            if val in map1:
                map1[val] += 1
            else :
                map1[val] = 1
        # print(map1)

        for i, val in enumerate(nums2) :
            if val in map2:
                map2[val] += 1
            else :
                map2[val] = 1
        # print(map2)

        intersectKeys = set(map1.keys()) & set(map2.keys())
        # print(intersectKeys)

        for key in intersectKeys :
            times = min(map1[key], map2[key])

            for t in range(times) :
                res.append(key)

        return res
    
sol = Solution()
res = sol.intersect([1,2,2,1], [2,2])
# res = sol.intersect([4,9,5], [9,4,9,8,4])
print(res)
