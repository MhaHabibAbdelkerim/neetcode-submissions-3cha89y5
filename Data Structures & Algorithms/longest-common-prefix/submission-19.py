class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            LCP = ""
            for i in range(len(strs[0])):
                for s in strs:
                    if i == len(s) or strs[0][i] != s[i]:
                        return LCP
                LCP += strs[0][i]
            return LCP