class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            middle = L + ((R - L) // 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                R = middle - 1
            else:
                L = middle + 1
        return L