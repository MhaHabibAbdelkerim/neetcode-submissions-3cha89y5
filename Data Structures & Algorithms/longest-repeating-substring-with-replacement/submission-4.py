class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count = {}
        Longest_Substring_K = 0

        L = 0
        for R in range(len(s)):
            Count[s[R]] = 1 + Count.get(s[R], 0)

            while (R - L + 1) - max(Count.values()) > k:
                Count[s[L]] -= 1
                L += 1

            Longest_Substring_K = max(Longest_Substring_K, R - L + 1)

        return Longest_Substring_K