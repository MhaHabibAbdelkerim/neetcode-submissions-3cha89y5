class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = list()
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            if count[nums[i]] > len(nums) // 3 and nums[i] not in res:
                res.append(nums[i])
        return res