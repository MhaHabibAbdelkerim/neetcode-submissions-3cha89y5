class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0] * length

        prefix[0] = nums[0]
        for i in range(1, length):
            prefix[i] = prefix[i - 1] + nums[i]
        
        for i in range(len(prefix)):
            if i == 0:
                Left_Sum = 0
                Right_Sum = prefix[-1] - prefix[i]
                if Left_Sum == Right_Sum:
                    return 0
            
            Left_Sum = prefix[i - 1]
            right_Sum = prefix[-1] - prefix[i]
        
            if Left_Sum == right_Sum:
                return i
        return -1