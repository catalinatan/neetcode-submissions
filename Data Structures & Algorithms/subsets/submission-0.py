class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        # decision tree
        def dfs(i):
            # leaf node, append entire subset and return without
            # running recursively
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1) # left branch 

            # deciision NOT to include nums[i]
            subset.pop()
            dfs(i + 1) # run recursively with empty subset 

        dfs(0) # start with 0 index
        return res 