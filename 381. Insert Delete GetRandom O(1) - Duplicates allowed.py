import collections
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values, self.indexs = [], collections.defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.values.append(val)
        self.indexs[val].add(len(self.values) - 1)
        return len(self.indexs[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.indexs[val]:
            index, lastval = self.indexs[val].pop(), self.values[-1]
            self.values[index] = lastval
            self.indexs[lastval].add(index)
            self.indexs[lastval].discard(len(self.values) - 1)
            self.values.pop()
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()