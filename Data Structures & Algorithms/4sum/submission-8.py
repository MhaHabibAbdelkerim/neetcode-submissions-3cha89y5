class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        Result = set()

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            TEMP = [nums[a], nums[b], nums[c], nums[d]]
                            Result.add(tuple(sorted(TEMP)))
        
        return [list(x) for x in Result]