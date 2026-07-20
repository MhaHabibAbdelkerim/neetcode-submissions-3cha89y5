class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Index_Value_Num1 = {num : i for i, num in enumerate(nums1)}
        result_array = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            current_number = nums2[i]
            while stack and stack[-1] < current_number:
                val = stack.pop()
                Index = Index_Value_Num1[val]
                result_array[Index] = current_number
            if current_number in Index_Value_Num1:
                stack.append(current_number)
        return result_array