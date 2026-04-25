class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 
        maxArea = 0

        while l < r and r < len(heights):  
            minH = min(heights[l], heights[r])
            maxArea = max(maxArea, (r - l) * minH)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1 
            else:
                r -= 1 

        return maxArea