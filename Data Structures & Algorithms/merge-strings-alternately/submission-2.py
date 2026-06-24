class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L, R = 0, 0
        res = []
        while L < len(word1) and R < len(word2):
          res.append(word1[L])
          res.append(word2[R])
          L += 1
          R += 1
        res.append(word1[L:])
        res.append(word2[R:])
        return "".join(res)