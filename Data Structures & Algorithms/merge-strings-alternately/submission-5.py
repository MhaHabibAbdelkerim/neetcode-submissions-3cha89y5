class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        OutPut = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            OutPut.append(word1[i])
            i += 1
            OutPut.append(word2[j])
            j += 1
        OutPut.append(word1[i:])
        OutPut.append(word2[j:])
        return "".join(OutPut)