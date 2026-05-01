class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_water = 0
        while i < j:
            area = min(heights[i] , heights[j]) * (j-i)
            max_water = max(max_water , area)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return max_water
        