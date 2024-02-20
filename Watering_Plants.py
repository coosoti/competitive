class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        can = capacity
        for i, x in enumerate(plants):
            if can < x:
                step += 2 * i
                can = capacity
            step += 1
            can -= x
        return step