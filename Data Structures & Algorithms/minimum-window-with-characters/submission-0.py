from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        if len(t) > len(s):
            return res

        t_count, s_count = Counter(t), Counter()
        have, need = 0, len(t_count)
        min_length = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1
            
            if c in t_count and s_count[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    res = s[l : r + 1]
                
                # shrink window
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                
        return res