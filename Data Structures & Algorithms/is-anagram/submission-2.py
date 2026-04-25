class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for idx in range(len(s)): 
            dict1[s[idx]] = 1 + dict1.get(s[idx], 0)
            dict2[t[idx]] = 1 + dict2.get(t[idx], 0)
        return dict1 == dict2 
        