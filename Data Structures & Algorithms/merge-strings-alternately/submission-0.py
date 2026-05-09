class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        new_word = ""
        while l < len(word1) and r < len(word2):
            new_word += word1[l]
            l += 1
            new_word += word2[r]
            r += 1
        
        if len(word1) <= len(word2):
            new_word += word2[r:]
        else:
            new_word += word1[l:]
        return new_word
            