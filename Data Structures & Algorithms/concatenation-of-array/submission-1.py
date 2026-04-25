class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(2 * n):
            if i < n: 
                ans.append(nums[i])
            else:
                n_i = i - n 
                ans.append(nums[n_i])
        return ans