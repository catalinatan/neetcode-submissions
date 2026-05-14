class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation means that exact order doesnt matter but like the matching letters has to be consecutive
        # brute force solution would be to make all permutations of s1 and check it against s2
        # can be a variable sliding window that checks if letter is indeed matching with s1
        # and then like remove from the s1 copy so if its empty then it means its in s2

        # frequency of char need to match for permutation
        # if u use deque or set it doesnt consider duplicate numbers

        # since u need exactly len(s1) chars to match the window must be fixed

        if len(s1) > len(s2): 
            return False

        s1_count = [0] * 26 
        window_count = [0] * 26  # window of s2

        # build initial window and s1 counts
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1 
            window_count[ord(s2[i])-ord('a')] += 1

        # count how many pos matches
        matches = 0 
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1 

        # slide window
        for r in range(len(s1), len(s2)):
            if matches == 26: # exactly the same order and permutation
                return True
        
            # add new char at right
            index = ord(s2[r]) - ord('a')
            window_count[index] += 1 
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] - 1 == s1_count[index]:  # was equal, now too many
                matches -= 1
            
            # Remove old character at left (l = r - len(s1))
            index = ord(s2[r - len(s1)]) - ord('a')
            window_count[index] -= 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] + 1 == s1_count[index]:  # was equal, now too few
                matches -= 1

        return matches == 26