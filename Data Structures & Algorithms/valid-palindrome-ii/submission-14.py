class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        def is_valid(L, R):
            while L <= R:
                if s[L] != s[R]: return False
                L += 1
                R -= 1
            return True

        while L <= R:
            if s[L] != s[R]:
                return (is_valid(L, R - 1) or is_valid(L + 1, R))
            L += 1
            R -= 1

        return True