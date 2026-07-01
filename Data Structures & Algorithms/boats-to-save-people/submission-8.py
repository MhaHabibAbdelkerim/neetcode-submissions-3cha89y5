class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        k = 0
        people.sort()
        L, R = 0, len(people) - 1
        while L <= R:
            if people[L] + people[R] > limit:
                R -= 1
                k += 1
            elif people[L] + people[R] < limit:
                R -= 1
                L += 1
                k += 1
            else:
                R -= 1
                L += 1
                k += 1

        return k