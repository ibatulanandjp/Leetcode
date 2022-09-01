# Working for only a specific set of test cases, NOT ALL

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 

        for i in range(len(gas)):
            tank = 0

            if gas[i] >= cost[i]:
                # print("---")
                # print("Gas", gas[i])
                # print("Cost", cost[i])

                tank += gas[i]

                flag = 0
                j = i
                for _ in range(len(gas)):
                    
                    # print("Tank", tank)
                    if tank < cost[j] :
                        flag = 1
                        break

                    tank = tank - cost[j] + gas[(j+1)%len(gas)]
                    if tank <= 0:
                        # print("Flag set")
                        flag = 1
                        break

                    j = (j+1)%len(gas)

                if flag == 0 and tank >= gas[i]:
                    return i

        return -1

sol = Solution()
# res = sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) #3
# res = sol.canCompleteCircuit([2,3,4], [3,4,3]) #-1
# res = sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]) #4
res = sol.canCompleteCircuit([2], [2]) #0
print(res)