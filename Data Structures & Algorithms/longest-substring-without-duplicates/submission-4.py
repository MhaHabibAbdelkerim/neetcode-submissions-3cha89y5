class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L_Longest_Substring = 0
        CharSet = set()

        L = 0
        for R in range(len(s)):
            while s[R] in CharSet:
                CharSet.remove(s[L])
                L += 1
            L_Longest_Substring = max(L_Longest_Substring, R - L + 1)
            CharSet.add(s[R])

        return L_Longest_Substring