class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        L, R  = 0, 0 

        while L < len(word1) and R < len(word2):
            result.append(word1[L])
            result.append(word2[R])
            L, R = L + 1, R + 1
        
        result.append(word1[L:])
        result.append(word2[R:])
        return "".join(result)