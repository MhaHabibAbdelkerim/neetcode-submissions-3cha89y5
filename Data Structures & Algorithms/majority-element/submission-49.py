class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Count = {}

        for i in range(len(nums)):
            Count[nums[i]] = 1 + Count.get(nums[i], 0)

            if Count[nums[i]] > len(nums) / 2:
                return nums[i]