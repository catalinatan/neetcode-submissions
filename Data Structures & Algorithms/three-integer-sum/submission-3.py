class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # so it can be any combination of i, j, k brute force would be 3 for loops over the indices over
        # the length of the nums array for each indice

        # rules: 
        # nums[i] != nums[j] != nums[k]
        # i != j != k 
        # nums[i] + nums[j] + nums[k] == 0 
        # no duplicate triplets ? use set

        res = []
        if not nums:
            return res
        
        # sort the array
        nums.sort()
        
        for i in range(len(nums) - 2):
            # dont need to double check duplicates 
            # if the index first index i is alr duplicate of
            # the previous one then gotta skip
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # normal 2 pointers, i+1, and end 
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0: # alr sorted array so if sum is less than 0, j+1 takes a larger
                    # number from the nums array
                    j += 1
                elif total > 0: # alr sorted array so if sum is more than 0, k-1 takes a 
                    # smaller number from the nums array 
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]]) # add to result if it passes the previous statements
                    # automatically means that its nums[i] + nums[j] + nums[k] == 0 

                    # duplicate handling on j and k 
                    while j < k and nums[j] == nums[j+1]: # skip if the next one is a duplicate
                        j += 1
                    while j < k and nums[k] == nums[k-1]: # skip if current k is the same as previous
                        k -= 1
                    
                    # its not double skipping cos e.g. j can point to j+1 (which is the last duplicate) so u need to 
                    # skip it to make the triplet valid
                    j += 1
                    k -= 1
            
        return res