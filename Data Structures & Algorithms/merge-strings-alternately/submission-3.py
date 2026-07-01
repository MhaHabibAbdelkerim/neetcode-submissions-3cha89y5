class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        L, R = 0, 0
        while L < len(word1) and R < len(word2):
          res.append(word1[L])
          L += 1
          res.append(word2[R])
          R += 1

        res.append(word1[L:])
        res.append(word2[R:])

        return "".join(res)