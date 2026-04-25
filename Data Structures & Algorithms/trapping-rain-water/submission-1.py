class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        maxArea = 0 

        while l < r and r < len(height):
            # shift the pointer with the min. val (so no need explicit min function)
            # update maxl and maxr
            if maxL < maxR: 
                l += 1 
                maxL = max(maxL, height[l])
                maxArea += maxL - height[l]
            else:
                r -= 1 
                maxR = max(maxR, height[r])
                maxArea += maxR - height[r]
                
        return maxArea

        
                
