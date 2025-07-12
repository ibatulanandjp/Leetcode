# Method: Use sorting to find the median
# TC: O(n logn) for addNum, O(n logn) for findMedian
# SC: O(n) for storing the numbers
class MedianFinder:

    def __init__(self):
        self.nums = []      

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        nlen = len(self.nums)

        mid = nlen // 2
        if nlen % 2 == 0:
            return (self.nums[mid-1] + self.nums[mid]) / 2
        return self.nums[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()