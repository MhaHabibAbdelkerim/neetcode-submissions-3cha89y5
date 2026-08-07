class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L_Longest_Substring = 0
        Window = set()

        L = 0
        for R in range(len(s)):
            while s[R] in Window:
                Window.remove(s[L])
                L += 1 

            Window.add(s[R])
            L_Longest_Substring = max(L_Longest_Substring, R - L + 1)
            
        return L_Longest_Substring
