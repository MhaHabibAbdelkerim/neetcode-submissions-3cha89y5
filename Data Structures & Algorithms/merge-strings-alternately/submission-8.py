class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_array = []

        L, R = 0, 0

        while L < len(word1) and R < len(word2):
            result_array.append(word1[L])
            result_array.append(word2[R])
            L, R = L + 1, R + 1

        result_array.append(word1[L:])
        result_array.append(word2[R:])

        return "".join(result_array)