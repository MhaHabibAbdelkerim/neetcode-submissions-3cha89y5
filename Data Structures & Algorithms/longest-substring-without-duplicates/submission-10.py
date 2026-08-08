class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Window = set()
        Longest_Substring = 0

        L = 0
        for R in range(len(s)):
            while s[R] in Window:
                Window.remove(s[L])
                L += 1
            
            Window.add(s[R])
            Longest_Substring = max(Longest_Substring, R - L + 1)
        return Longest_Substring