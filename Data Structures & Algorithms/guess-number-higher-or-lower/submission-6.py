# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Defining left and right ptrs
        Left_Ptr, Right_Ptr = 1, n

        # While Loop
        while Left_Ptr <= Right_Ptr:
            middle = (Left_Ptr + Right_Ptr) // 2

            # guess
            guessed_Number = guess(middle)
            if guessed_Number == 0:
                return middle
            elif guessed_Number == -1:
                Right_Ptr = middle - 1
            else:
                Left_Ptr = middle + 1