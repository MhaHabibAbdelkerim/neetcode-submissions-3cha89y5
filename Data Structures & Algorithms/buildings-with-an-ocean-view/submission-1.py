class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        OutPut_array = []
        for i in range(len(heights)):
            Max_number = 0
            for j in range(i + 1, len(heights)):
                if Max_number < heights[j]:
                    Max_number = heights[j]
            if heights[i] > Max_number:
                OutPut_array.append(i)
        return OutPut_array