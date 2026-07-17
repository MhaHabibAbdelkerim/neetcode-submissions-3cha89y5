class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            Left_Substring = s[:i]
            Right_Substring = s[i:]
            left_score = 0
            right_score = 0

            for i in range(len(Left_Substring)):
                if Left_Substring[i] == "0":
                    left_score += 1
                continue

            for i in range(len(Right_Substring)):
                if Right_Substring[i] == "1":
                    right_score += 1
                continue

            total = left_score + right_score
            max_score = max(max_score, total)
        return max_score
