class Solution:
    # Brute force approach:
    # There are O(n^2) possible substrings.
    # For each substring, checking whether it is a palindrome
    # using two pointers takes O(n) time.
    #
    # Total time complexity:
    # O(n^2) * O(n) = O(n^3)

    # Better approach:
    # Expand around every possible center.
    #
    # For each index i:
    # 1. Check odd-length palindromes  -> center at (i, i)
    # 2. Check even-length palindromes -> center at (i, i + 1)
    #
    # Since every expansion is linear and we do this for n centers,
    # the overall time complexity becomes O(n^2).
    #
    # Space complexity: O(1)

    def expand(self, s, l, r):
        count = 0

        # Continue expanding while:
        # 1. pointers are within bounds
        # 2. characters are equal
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Every successful expansion forms a palindrome
            count += 1

            # Expand outward
            l -= 1
            r += 1

        return count

    def countSubstrings(self, s):
        count = 0

        for i in range(len(s)):
            # Odd-length palindromes
            # Example: "aba"
            count += self.expand(s, i, i)

            # Even-length palindromes
            # Example: "abba"
            count += self.expand(s, i, i + 1)

        # Palindromes do NOT need to be unique.
        # If they start/end at different indices,
        # they are counted as different substrings.
        return count