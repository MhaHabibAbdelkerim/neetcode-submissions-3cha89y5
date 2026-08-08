class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Longest_C_Prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return Longest_C_Prefix
            Longest_C_Prefix += strs[0][i]
        
        return Longest_C_Prefix