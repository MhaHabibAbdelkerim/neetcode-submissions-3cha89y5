class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Index_Value_Num1 = {num : i for i, num in enumerate(nums1)}
        result_array = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in Index_Value_Num1:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    Index = Index_Value_Num1[nums2[i]]
                    result_array[Index] = nums2[j]
                    break
        return result_array