class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result_array = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[result_array[-1]]:
                result_array.append(i)

        L, R = 0, len(result_array) - 1
        while L <= R:
            result_array[L], result_array[R] = result_array[R], result_array[L]
            L += 1
            R -= 1

        return result_array