class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        list_len = len(heights)
        middle_len = list_len //2
        for i in range(list_len):
            for j in range(list_len-1, -1, -1):
                final_height = min(heights[i], heights[j])
                step = abs(j-i)
                area = final_height * step
                if area > max_area:
                    max_area = area
        return max_area