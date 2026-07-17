# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            middle = L + ((R - L) // 2)
            res = guess(middle)
            if res > 0:
                L = middle + 1
            elif res < 0:
                R = middle - 1
            else:
                return middle