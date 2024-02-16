import random

class RandomizedSet:

    def __init__(self):
        """initialize the class"""
        self.my_list = []

    def insert(self, val: int) -> bool: # O(n) both time and space
        if val not in self.my_list:
            self.my_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool: # O(n) both time and space
        if val in self.my_list:
            self.my_list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:  # O(1)
        return random.choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()