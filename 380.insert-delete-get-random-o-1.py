#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (45.43%)
# Likes:    1882
# Dislikes: 130
# Total Accepted:    180.2K
# Total Submissions: 394.3K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' + '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
#
#
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each
# element must have the same probability of being returned.
#
#
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();
#
#
#

# @lc code=start
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.idxs = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idxs:
            return False
        else:
            self.vals.append(val)
            self.idxs[val] = len(self.vals) - 1
            self.count += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idxs:
            idx = self.idxs[val]
            del self.idxs[val]
            self.vals[idx] = None
            self.count -= 1
            self._clean()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        while True:
            idx = random.randint(0, len(self.vals) - 1)
            val = self.vals[idx]
            if val is not None:
                return val

    def _clean(self):
        if len(self.vals) >= 4 and len(self.vals) > 2 * self.count:
            self.vals = [i for i in self.vals if i is not None]
            self.idxs = {val: idx for idx, val in enumerate(self.vals)}
            self.count = len(self.vals)


# @lc code=end
if __name__ == "__main__":
    randomSet = RandomizedSet()
    true, false = True, False

    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    assert randomSet.insert(1) == true

    # Returns false as 2 does not exist in the set.
    assert randomSet.remove(2) == false

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    assert randomSet.insert(2) == true

    # getRandom should return either 1 or 2 randomly.
    assert randomSet.getRandom() in [1, 2]

    # Removes 1 from the set, returns true. Set now contains [2].
    assert randomSet.remove(1) == true

    # 2 was already in the set, so return false.
    assert randomSet.insert(2) == false

    # Since 2 is the only number in the set, getRandom always return 2.
    assert randomSet.getRandom() in [2]
