from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

# Example usage
nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(Solution().search(nums, target))  # Output: 3