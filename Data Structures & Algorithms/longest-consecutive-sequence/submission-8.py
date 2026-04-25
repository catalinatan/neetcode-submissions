class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        print(sorted_nums)
        sequence_count = 1 
        max_count = 0
        item_count = 0

        while item_count < len(sorted_nums):
            for item in sorted_nums:
                if item + 1 in sorted_nums: 
                    sequence_count += 1 
                else:
                    if sequence_count > max_count: 
                        max_count = sequence_count
                    sequence_count = 1
                item_count += 1 
        return max_count