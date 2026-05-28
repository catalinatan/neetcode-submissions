class Solution:
    def countSubstrings(self, s):
        count = 0

        def expand(l, r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)

        return count