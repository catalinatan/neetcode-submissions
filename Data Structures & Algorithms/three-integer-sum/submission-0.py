class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output_set = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        unsorted_list = [nums[i], nums[j], nums[k]]
                        sorted_tuple = tuple(sorted(unsorted_list))
                        output_set.add(sorted_tuple)
        output_list = list(list(item) for item in output_set)
        if output_list:
            return output_list
        else:
            return []