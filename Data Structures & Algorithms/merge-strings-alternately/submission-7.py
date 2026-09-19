class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j  = 0, 0
        result_array = []
        while i < len(word1) and j < len(word2):
            result_array.append(word1[i])
            result_array.append(word2[j])
            i += 1
            j += 1
        result_array.append(word1[i:])
        result_array.append(word2[j:])
        return "".join(result_array)