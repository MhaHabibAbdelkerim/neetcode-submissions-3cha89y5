class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                S_Temp, S_Index = stack.pop()
                res[S_Index] = (i - S_Index)
            stack.append([t, i])
        return res