class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for I, T in enumerate(temperatures):
            while stack and T > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (I - stackInd)
            stack.append([T, I])
        return res