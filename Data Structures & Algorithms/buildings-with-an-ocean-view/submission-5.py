class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        OutPut_array = [len(heights) - 1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[OutPut_array[-1]]:
                OutPut_array.append(i)
        OutPut_array.reverse()
        return OutPut_array