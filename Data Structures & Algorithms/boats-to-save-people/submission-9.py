class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        K = 0
        people.sort()
        L, R = 0, len(people) - 1
        while L <= R:
            if people[L] + people[R] > limit:
                R -= 1
                K += 1
            
            else:
                L += 1
                R -= 1
                K += 1
        return K