class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        Leftsum = 0
        for i in range(len(nums)):
            Rightsum = total - Leftsum - nums[i]
            if Leftsum == Rightsum:
                return i
            Leftsum += nums[i]
        return -1