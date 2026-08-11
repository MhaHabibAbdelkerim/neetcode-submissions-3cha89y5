class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result_array = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[result_array[-1]]:
                result_array.append(i)
        result_array.reverse()
        return result_array