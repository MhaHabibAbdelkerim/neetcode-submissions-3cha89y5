class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if not s[L].isalnum():
                L = L + 1
            elif not s[R].isalnum():
                R = R - 1
            elif s[L].lower() == s[R].lower():
                L = L + 1
                R = R - 1
            else:
                return False
        
        return True