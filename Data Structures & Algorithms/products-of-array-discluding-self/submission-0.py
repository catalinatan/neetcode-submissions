class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = []
        
        for idx in range(len(nums)):
            start_idx = min(0, idx)
            mid_idx = idx 
            first_product = 1
            for idx in range(start_idx, mid_idx):
                first_product *= nums[idx]
            end_idx = len(nums)
            for idx in range(mid_idx+1, end_idx):
                first_product *= nums[idx]
            output_list.append(first_product)
        print(output_list)
        return output_list