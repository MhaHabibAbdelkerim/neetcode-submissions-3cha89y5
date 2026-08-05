class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        Longest_Substring = 0

        L = 0 
        maxFrequency = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxFrequency = max(maxFrequency, count[s[R]])

            while (R - L + 1) - maxFrequency > k:
                count[s[L]] -= 1
                L += 1

            Longest_Substring = max(Longest_Substring, R - L + 1)
        return Longest_Substring