class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Longest_substring = 0
        HashSet = set()

        L = 0
        for R in range(len(s)):
            while s[R] in HashSet:
                HashSet.remove(s[L])
                L += 1
            HashSet.add(s[R])
            Longest_substring = max(Longest_substring, R - L + 1)
        
        return Longest_substring