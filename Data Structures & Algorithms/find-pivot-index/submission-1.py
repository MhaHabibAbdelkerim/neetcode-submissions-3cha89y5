class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        LeftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - LeftSum
            if LeftSum == rightSum:
                return i
            LeftSum += nums[i]
        return -1