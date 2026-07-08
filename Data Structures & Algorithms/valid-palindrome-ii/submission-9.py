class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        def is_Palindrome(L, R):
            while L <= R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
        
        while L <= R:
            if s[L] != s[R]:
                return (is_Palindrome(L + 1, R) or is_Palindrome(L, R - 1))
            L += 1
            R -= 1
        
        return True