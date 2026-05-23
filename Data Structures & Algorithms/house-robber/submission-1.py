class Solution:
    def rob(self, nums: List[int]) -> int:
        # Can't rob adjacent houses (i-1 or i+1)
        # So for each house you have a choice to rob or not
        # 1) If you rob, that means that its the best combo up till house (i-2) since (i-1) is not allowed (adjacent) PLUS
        # you get the money from the house u rob so thats nums[i] + best_sum till i-2
        # 2) if you don't rob, that means taht its the best combo up till house (i-1)

        # So now in dp, you store 2 variables
        # you'll update prev2 with prev1, and prev1 with the sum of the best combo so far based on conditions 1)/2)
        # we keep track of the new best each time and we want to maximise the money so maximise between choices 1) and 2)
        # cause you can only choose 1
        prev2, prev1 = 0, 0
        new_best = 0 

        # you loop over all the choices and choose whether or not to rob and keep track of the best combination sum so far
        for n in range(len(nums)):
            new_best = max(nums[n]+prev2, prev1)
            prev2, prev1 = prev1, new_best
        return new_best