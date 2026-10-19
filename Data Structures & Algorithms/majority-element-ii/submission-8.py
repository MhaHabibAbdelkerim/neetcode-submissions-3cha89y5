class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       output = set()
       HashMap = {}

       for n in nums:
        HashMap[n] = HashMap.get(n, 0) + 1
        if HashMap[n] > len(nums) / 3:
            output.add(n)

       return list(output)