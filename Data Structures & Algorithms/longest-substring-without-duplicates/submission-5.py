class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Longest_Substring = 0
        Window = set()
        L = 0

        for R in range(len(s)):
            while s[R] in Window:
                Window.remove(s[L])
                L += 1
            
            Longest_Substring = max(Longest_Substring, R - L + 1)
            Window.add(s[R])

        return Longest_Substring