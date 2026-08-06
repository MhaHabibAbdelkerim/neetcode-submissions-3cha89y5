class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count_of_Values = {}
        Longest_Substring_K = 0

        L = 0
        for R in range(len(s)):
            Count_of_Values[s[R]] = 1 + Count_of_Values.get(s[R], 0)

            while (R - L + 1) - max(Count_of_Values.values()) > k:
                Count_of_Values[s[L]] -= 1
                L += 1

            Longest_Substring_K = max(Longest_Substring_K, R - L + 1)

        return Longest_Substring_K 
