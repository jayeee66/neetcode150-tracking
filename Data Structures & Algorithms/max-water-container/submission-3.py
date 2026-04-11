class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = (min(heights[l], heights[r])) * (r - l)
            if area > res:
                res = area
                
            # To find a larger area. Since moving either pointer 
            # decreases the width (r - l), we must try to increase the height.
            # Therefore, we always move the pointer pointing to the shorter bar,
            # because the shorter bar is the "bottleneck" that limits the area.
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return res
