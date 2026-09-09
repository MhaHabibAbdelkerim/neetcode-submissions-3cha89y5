class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_array = [0] * len(temperatures)
        stack = [] # pair: [Temperature, Index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                STEMP, SINDEX = stack.pop()
                result_array[SINDEX] = i - SINDEX
            stack.append([t, i])

        return result_array