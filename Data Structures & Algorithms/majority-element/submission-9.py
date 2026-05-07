class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for nums in nums:
            if count == 0:
                ans = nums
            
            if ans == nums:
                count += 1

            else:
                count -=1 

        return ans

