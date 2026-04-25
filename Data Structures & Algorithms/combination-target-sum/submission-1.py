# search for different combinations --> use dfs

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # cur is [2, 2, 2] what's the current variable
        # i is the node
        # total is the sum of the array 
        def dfs(i, cur, total):
            # base case 
            if total == target:
                res.append(cur.copy()) # use copy cos vof modification
                return

            # if impossible if i (index of value in nums) is out of bounds or total exceeds target
            if i >= len(nums) or total > target: 
                return
            
            # include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # not changing i cos u can add duplicate numbers but not duplicate combinations
            
            # don't include nums[i]
            cur.pop()
            dfs(i +1, cur, total) # can't include any occurences of i 

        dfs(0, [], 0)
        return res