class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result_array = []
        
        for i in range(len(heights)):
            Max = 0
            for j in range(i + 1, len(heights)):
                if Max < heights[j]:
                    Max = heights[j]
            if Max < heights[i]:
                result_array.append(i)
        return result_array