class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalnum()==True:
                word += char.lower()
        if word[::-1] == word:
            return True
        else:
            return False

        