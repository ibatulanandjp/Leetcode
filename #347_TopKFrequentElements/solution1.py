from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        res=[]
        
        for i in range(len(nums)):
            if nums[i] in count_map:
                count_map[nums[i]] += 1
            else:
                count_map[nums[i]] = 1
                
        count_map = self.sort_map(count_map)
        # print(count_map)
        
        for i in range(k):
            res.append(count_map[i][0])
            
        # print(res)
        return res
                
    def sort_map(self, count_map:dict) -> dict:
        return sorted(count_map.items(), key=lambda item: item[1], reverse=True)
            
            