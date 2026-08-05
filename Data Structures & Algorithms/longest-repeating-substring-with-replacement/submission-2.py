class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count = {}
        Longest_Substring = 0

        Left = 0
        for Right in range(len(s)):
            Count[s[Right]] = 1 + Count.get(s[Right], 0)

            while (Right - Left + 1) - max(Count.values()) > k:
                Count[s[Left]] -= 1
                Left += 1

            Longest_Substring = max(Longest_Substring, Right - Left + 1)

        return Longest_Substring
