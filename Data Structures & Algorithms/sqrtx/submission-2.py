class Solution:
    def mySqrt(self, x: int) -> int:

        # Initialize search space
        Left_Ptr, Right_Ptr = 0, x
        Result = 0

        while Left_Ptr <= Right_Ptr:
            middle = (Left_Ptr + Right_Ptr) // 2
            if middle ** 2 > x:
                Right_Ptr = middle - 1
            elif middle ** 2 < x:
                Left_Ptr = middle + 1
                Result = middle
            else:
                return middle
        return Result