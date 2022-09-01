from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0    # for balance of the tank
        deficit = 0     # for deficit in the tank
        start = 0   # for starting index

        for i in range(len(gas)):
            tank = tank - cost[i] + gas[i]

            if tank < 0:
                deficit += tank
                start = i+1
                tank = 0

        if tank + deficit >= 0:
            return start
        return -1

sol = Solution()
res = sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) #3
# res = sol.canCompleteCircuit([2,3,4], [3,4,3]) #-1
# res = sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]) #4
# res = sol.canCompleteCircuit([2], [2]) #0
print(res)