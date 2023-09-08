from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1], [1, 1]]

        if numRows <= 2:
            return res[:numRows]

        else:
            for i in range(2, numRows):
                temp = []

                for j in range(i+1):
                    # Append 1 for the 1st and last element
                    if j==0 or j==i:
                        temp.append(1)
                    # Append sum of previous row (j-1)th and jth element
                    else:
                        temp.append(res[-1][j-1] + res[-1][j])

                res.append(temp)

        return res


sol = Solution()
res = sol.generate(5)
print(res)
