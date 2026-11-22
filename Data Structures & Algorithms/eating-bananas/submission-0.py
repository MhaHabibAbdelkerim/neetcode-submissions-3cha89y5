class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the search space
        Left_Ptr, Right_Ptr = 1, max(piles)
        Minimum = 0

        while Left_Ptr <= Right_Ptr:
            # Getting the middle value
            middle = (Left_Ptr + Right_Ptr) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/middle)
            if hours > h:
                Left_Ptr = middle + 1
            else:
                Right_Ptr = middle - 1

        return Left_Ptr
          