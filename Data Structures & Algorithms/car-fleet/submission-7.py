class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        Stack = []

        for p, s in sorted(pairs)[::-1]:
            Stack.append((target - p) / s)
            while len(Stack) >= 2 and Stack[-1] <= Stack[-2]:
                Stack.pop()
        
        return len(Stack)