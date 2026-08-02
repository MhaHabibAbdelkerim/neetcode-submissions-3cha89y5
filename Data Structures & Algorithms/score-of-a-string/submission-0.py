class Solution:
    def scoreOfString(self, s: str) -> int:
        Sum = 0
        for i in range(1, len(s)):
            Sum += abs(ord(s[i]) - ord(s[i - 1]))
        return Sum