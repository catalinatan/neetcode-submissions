class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lower + upper bound for k 
        low, upp = 1, max(piles) # never needs to eat faster than the largest pile
        best_k = upp

        while low <= upp: 
            mid = (low + upp) // 2 

            sum_of_hrs = 0 
            for pile in piles: 
                sum_of_hrs += (pile + mid - 1) // mid # this rounds up 
            
            if sum_of_hrs <= h: 
                best_k = min(best_k, mid)
                upp = mid - 1 
            else:
                low = mid + 1 
           
                
        return best_k

        
