class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        Result_array = []

        while i < len(word1) and j < len(word2):
            Result_array.append(word1[i])
            Result_array.append(word2[j])
            i += 1
            j += 1

        Result_array.append(word1[i:])
        Result_array.append(word2[j:])
        return "".join(Result_array)