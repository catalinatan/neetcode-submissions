class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        seen = set()

        while n != 1:
            if n in seen:
                return False
                
            seen.add(n)

            n_sum = 0
            for d in str(n):
                n_sum += int(d) ** 2
            n = n_sum

        return True
