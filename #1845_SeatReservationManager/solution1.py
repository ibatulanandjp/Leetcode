# Method: Use Counter (to speed-up) and Priority Queue as data structure
# TC: 
# reserve: O(1) average using counter, but O(log n) when using min-heap; 
# unreserve: O(1) average using counter, but O(log n) when using min-heap; 
# SC: O(n)

import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seatPQ = []
        self.last = 0

    def reserve(self) -> int:
        if not self.seatPQ:
            self.last += 1
            return self.last
        return heapq.heappop(self.seatPQ)
        
    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.seatPQ, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)