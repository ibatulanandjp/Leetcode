# Method: Use Mathematical approach - finish point should be reachable if t >= max(width, height)
# TC: O(1)
# SC: O(1
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(sx - fx)
        height = abs(sy - fy)
        if width == 0 and height == 0 and t == 1:
            return False
        return t >= max(width, height)