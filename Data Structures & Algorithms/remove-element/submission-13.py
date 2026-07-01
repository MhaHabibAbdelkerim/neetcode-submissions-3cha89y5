class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_arr = []
        for n in nums:
            if n != val:
                temp_arr.append(n)
        for i in range(len(temp_arr)):
            nums[i] = temp_arr[i]
        return len(temp_arr)