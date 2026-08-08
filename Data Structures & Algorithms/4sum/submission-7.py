class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        Result_array = set()
        nums.sort()

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            FourSum = [nums[a], nums[b], nums[c], nums[d]]
                            Result_array.add(tuple(FourSum))

        return [list(i) for i in Result_array]