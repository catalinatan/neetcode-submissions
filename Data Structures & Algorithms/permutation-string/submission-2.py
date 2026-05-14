from collections import Counter
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

        # Counter(s2[:len(s1)])
        # makes a frequency dictionary for the first len(s1) chars of s2 using counter
        s1_count, s2_count = Counter(s1), Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for r in range(len(s1), len(s2)):
            s2_count[s2[r]] += 1
            s2_count[s2[r - len(s1)]] -= 1
            # need to delete because the dictionaries wouldnt be exactly the same
            if s2_count[s2[r - len(s1)]] == 0:
                del s2_count[s2[r - len(s1)]]
            
            if s1_count == s2_count:
                return True
            
        return False