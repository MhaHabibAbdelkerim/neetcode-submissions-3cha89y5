class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize the search space
        left_Ptr, right_Ptr = 0, x
        Result = 0

        while left_Ptr <= right_Ptr:
            middle = (left_Ptr + right_Ptr) // 2
            if middle * middle > x:
                right_Ptr = middle - 1
            elif middle * middle < x:
                left_Ptr = middle + 1
                Result = middle
            else:
                return middle
        return Result

