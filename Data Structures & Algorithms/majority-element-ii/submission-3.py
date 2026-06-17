class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

            if count[n] > len(nums) / 3:
                if n in res:
                    pass
                else:
                    res.append(n)
        return res
            