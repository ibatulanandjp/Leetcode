from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitAlphabetMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        for i in digits:
            res = self.cartesianProduct(res, digitAlphabetMap.get(i))         
        return res


    def cartesianProduct( self, list1: List[str], list2: List[str] ) -> List[str]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Cartesian product of the 2 lists
        product = []
        for i in list1:
            for j in list2:
                product.append(i+j)
        return product


sol = Solution()
res = sol.letterCombinations("23") #["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(res)