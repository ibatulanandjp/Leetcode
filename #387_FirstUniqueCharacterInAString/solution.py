class Solution:
    def firstUniqueChar(self, s: str) -> int:
        map = {}

        # Create a map of {element: count}
        for char in s:
            if char in map:
                map[char] += 1

            else:
                map[char] = 1

        # Iterate over elements in the map
        for i in map:
            # If the element's value is "1", return index of the key from the string 
            if map.get(i) == 1:
                return s.index(i)
            
        return -1


sol = Solution()
res = sol.firstUniqueChar("aabb")
print(res)
