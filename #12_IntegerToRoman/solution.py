# Method: Hashmap to store the integer to roman mapping in descending order.
# Reduce the number and add the corresponding roman value to the result.
# TC: O(1)
# SC: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        ri_map = {
            1000: 'M', 900: 'CM',
            500: 'D', 400: 'CD',
            100: 'C', 90: 'XC',
            50: 'L', 40: 'XL',
            10: 'X', 9: 'IX',
            5: 'V', 4: 'IV',
            1: 'I',
        }
        res = ""

        for key, val in ri_map.items():
            while key <= num:
                res += val
                num -= key
        return res
