class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        
        while j >= 0:  # we still have elements from nums2 to place
            if i>= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i] # take from nums1 so increment that
                i -= 1 
            else:
                nums1[last] = nums2[j] # take from nums2 so increment that
                j -= 1
            last -= 1 # move last left
        
            

