class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count = {}
        Longest_Substring = 0

        Max_Frequency = 0
        L = 0
        for R in range(len(s)):
            Count[s[R]] = 1 + Count.get(s[R], 0)
            Max_Frequency = max(Max_Frequency, Count[s[R]])

            while (R - L + 1) - Max_Frequency > k:
                Count[s[L]] -= 1
                L += 1
            Longest_Substring = max(Longest_Substring, R - L + 1)

        return Longest_Substring