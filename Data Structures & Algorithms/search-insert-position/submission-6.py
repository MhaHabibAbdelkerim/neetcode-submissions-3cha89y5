class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        Left_Ptr, Right_Ptr = 0, len(nums) - 1

        while Left_Ptr <= Right_Ptr:
            middle = (Left_Ptr + Right_Ptr) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                Right_Ptr = middle - 1
            else:
                Left_Ptr = middle + 1
        return Left_Ptr