class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        # sort input array candidates so that 
        # all duplicate elements are adjacent 
        # [1, 2, 3, 1] --> [1, 1, 2, 3]

        # i is the index of candidates
        # shift i so that u won't add it multiple points
        # but gotta skip 1 in total u need to do while loop 

        # while i + 1 keep shifting it if its the same as i 

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 

            if total > target or i == len(candidates):
                return 
            
            # choice to add candidates[i]
            cur.append(candidates[i])

            dfs(i + 1, cur, total + candidates[i])

            # choice to skip candidates[i]
            cur.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res