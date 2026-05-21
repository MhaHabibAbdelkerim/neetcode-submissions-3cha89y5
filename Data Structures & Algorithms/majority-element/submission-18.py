class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for n in nums:
            majority[n] = nums.count(n)
        for k, v in majority.items():
            if v > len(nums) / 2:
                return k