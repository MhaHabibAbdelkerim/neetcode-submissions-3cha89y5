class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            quadruplet = tuple(sorted((nums[a], nums[b], nums[c], nums[d])))
                            res.add(quadruplet)
        return [list(x) for x in res]