class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # signs must be alternating for turbulent array 
        # can't be equal to each other either

        L, R = 0, 1 
        maxWin, prev = 1, ""
        # prev checks the sign 

        while R < len(arr):
            # EVEN case so to make it turbulent previous sign can't be >
            if arr[R-1] > arr[R] and prev != ">":
                maxWin = max(maxWin, R - L + 1)
                R += 1 
                prev = ">"
            
            elif arr[R-1] < arr[R] and prev != "<":
                maxWin = max(maxWin, R - L + 1)
                R += 1 
                prev = "<"
            # same sign as prev or = sign 
            else:
                if arr[R-1] == arr[R]:
                    R += 1 
                L = R - 1 
                prev = ""
    
        return maxWin
