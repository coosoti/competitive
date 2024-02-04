class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if letter not in s:
                return letter
        return ""
