class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Prevmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Prevmap:
                return [Prevmap[diff], i]
            Prevmap[n] = i
        return
            
