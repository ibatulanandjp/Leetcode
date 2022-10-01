class Solution:
    def numberOfWays(self, s: str) -> int:
        '''
        DP Solution
        '''
        _0, _1, _01, _10, _010, _101 = 0, 0, 0, 0, 0, 0

        # Iterate through the string
        for c in s:
            if c=="0":
                _0 += 1
                _10 += _1
                _010 += _01

            else:
                _1 += 1
                _01 += _0
                _101 += _10

        return _010 + _101