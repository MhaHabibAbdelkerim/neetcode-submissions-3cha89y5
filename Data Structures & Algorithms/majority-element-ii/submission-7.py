class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = set()
        Hashmap = {}

        for n in nums:
            Hashmap[n] = 1 + Hashmap.get(n, 0)
            if Hashmap[n] > len(nums) / 3:
                output.add(n)

        return list(output)
