class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result_array = []
        Count = {}

        for i in range(len(nums)):
            Count[nums[i]] = 1 + Count.get(nums[i], 0)
            if Count[nums[i]] > len(nums) / 3:
                if nums[i] not in result_array:
                    result_array.append(nums[i])

        return result_array