from itertools import accumulate
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:

        MOD = 10 ** 9 + 7
        n = len(strength)

        '''
        Calculate small element on the left and right
        Using monotonic stack approach
        '''
        # Next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                element = stack.pop()
                right[element] = i
            stack.append(i)
        print(right)

        # Next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                element = stack.pop()
                left[element] = i
            stack.append(i)
        print(left)

        '''
        Calculate sum for each wizard's strength
        Using Prefix of Prefix Sum Approach
        '''
        res = 0
        # Prefix sum of prefix sum
        acc = list(accumulate(accumulate(strength), initial=0))

        for i in range(n):
            l = left[i]
            r = right[i]

            # Use the formula
            l_acc = acc[i] - acc[max(l, 0)]
            r_acc = acc[r] - acc[i]

            ln = i-l
            rn = r-i

            res += strength[i] * (r_acc * ln - l_acc * rn)

        return res % MOD
