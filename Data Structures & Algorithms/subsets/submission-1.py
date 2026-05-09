class Solution:
    # array nums only contains unique integers so you don't actl need a set
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums): # leaf node
                res.append(subset.copy())
                return 

            # exclude nums[i]
            dfs(i+1)

            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            subset.pop() # backtrack

        dfs(0)
        return res
 