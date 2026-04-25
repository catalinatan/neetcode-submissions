class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        # build initial window counts
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # count how many character counts match
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # sliding window over s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right char
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            # remove left char
            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1

            l += 1

        return matches == 26
