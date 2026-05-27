class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 choices - either rob the current house and then add current house + sum up until house i-2
        # skip the current house so sum until house i-1
        # try to maximise between 2 choices

        prev2, prev1 = 0, 0
        new_best = 0
        for i in range(len(nums)):
            new_best = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, new_best
        return new_best

