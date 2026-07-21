class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Index_Value_Nums1 = {nums : i for i, nums in enumerate(nums1)}
        result_array = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                Value = stack.pop()
                Index = Index_Value_Nums1[Value]
                result_array[Index] = nums2[i]
            if nums2[i] in Index_Value_Nums1:
                stack.append(nums2[i])
        return result_array