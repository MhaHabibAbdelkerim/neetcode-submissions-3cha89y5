class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Longest_Substring = 0
        CharSet = set()

        L = 0
        for R in range(len(s)):
            while s[R] in CharSet:
                CharSet.remove(s[L])
                L += 1
            CharSet.add(s[R])
            Longest_Substring = max(Longest_Substring, R - L + 1)

        return Longest_Substring