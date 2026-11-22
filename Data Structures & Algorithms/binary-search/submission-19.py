class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Left, Right = 0, len(nums) - 1
        while Left <= Right:
            middle = (Left + Right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                Right = middle - 1
            else: 
                Left = middle + 1
        return -1
