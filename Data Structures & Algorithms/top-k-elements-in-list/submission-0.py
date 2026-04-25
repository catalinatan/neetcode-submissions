class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_dict = {}

        for idx in range(len(nums)):
            unique_dict[nums[idx]] = 1 + unique_dict.get(nums[idx], 0)

        print(unique_dict)
        unique_dict = dict(sorted(unique_dict.items(), key=lambda item: item[1], reverse=True))
        unique_num_list = list(unique_dict)
      
        output_list = []
        for no in range(k):
            num = unique_num_list[no]
            output_list.append(num)

        return output_list