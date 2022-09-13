from math import ceil
from random import random
from typing import List


class Solution:
    def sumZero(self, n:int) -> List[int]:
        list = []
        ctr = ceil(n/2)+1

        if n%2==1:
            ctr -= 1
            list.append(0)
        for i in range(1, ctr):
            list.append(i)
            list.append(-i)        
        return list

sol = Solution()
res = sol.sumZero(5)
print(res)