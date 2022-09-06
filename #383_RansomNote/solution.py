class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapRansomNote = {}
        mapMagazine = {}

        # Create a map of elements in the ransomNote string
        for i in ransomNote:
            if i in mapRansomNote:
                mapRansomNote[i] += 1
            else:
                mapRansomNote[i] = 1

        # Create a map of elements in the magazine string
        for i in magazine:
            if i in mapMagazine:
                mapMagazine[i] += 1
            else:
                mapMagazine[i] = 1


        # Iterate over the elements of RansomNote map
        for element in mapRansomNote:
            # print(element)
            # print(mapMagazine.get(element))
            # print(mapRansomNote.get(element))

            # If the ransomnote element is not in magazine map
            # OR (element is in magazine map and element's value is less than ransomNote element's value)
            if element not in mapMagazine or (element in mapMagazine and mapMagazine.get(element) < mapRansomNote.get(element)):
                return False


        return True

sol = Solution()
# res = sol.canConstruct("a", "b")
# res = sol.canConstruct("aa", "ab")
# res = sol.canConstruct("aa", "aab")
res = sol.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print(res)