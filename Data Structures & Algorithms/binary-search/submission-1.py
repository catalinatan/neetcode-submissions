class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            i = (l + r) // 2
            m = nums[i]

            if target == m:
                return i
            elif target < m:
                r = i - 1
            else:
                l = i + 1

        return -1




