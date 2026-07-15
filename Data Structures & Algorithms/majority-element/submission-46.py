class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = 1 + res.get(nums[i], 0)
            if res[nums[i]] > len(nums) // 2:
                return nums[i]
                