class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap to store frequencies of sums
        hashmap = {0 : 1}
        total = 0 
        res = 0 

        for n in nums:
            total += n 
            # prefix sum is prefix_sum[r] - prefix_sum[l-1] where r is current idx
            # we want prefix_sum[r] - prefix_sum[l-1] == k 
            # and we need to find prefix_sum[l-1]
            # so prefix_sum[l-1] = prefix_sum[r] - k 
            # since r is current index its basically the total
            target = total - k 

            # target changes each time as we move across basically the right pointer is moved each time 
            # then we calculate how many prefix sums that will equal to k from that right pointer 
            # since target changes each time we're not double counting
            res += hashmap.get(target, 0)
            hashmap[total] = hashmap.get(total,0) + 1 
    
        return res
