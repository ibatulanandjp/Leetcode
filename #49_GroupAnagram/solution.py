from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # A dictionary to store <sorted(str):List[index]>
        dict = {}
        res = []

        for i, s in enumerate(strs):
            temp = sorted(s)
            tempString = ""
            for k in temp:
                tempString += k
            # print(tempString)

            if tempString not in dict:
                # print("Not:", tempString)
                dict[tempString] = [i]
            else:
                # print("Already:", tempString)
                dict[tempString].append(i)
        # print("Dict:", dict)

        # Transform the dict in the list
        for key in dict:
            # print("Key:", key)
            curr = []
            for _index in dict[key]:
                curr.append(strs[_index])

            res.append(curr)

        return res


sol = Solution()
res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
