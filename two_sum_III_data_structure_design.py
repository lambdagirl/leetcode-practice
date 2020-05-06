# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:

# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, number: int) -> None:  #O(1)
        """
        Add the number to an internal data structure..
        """
        if number not in self.hash:
            self.hash[number] = 1
        else:
            self.hash[number] += 1

    def find(self, value: int) -> bool:  #O(N)
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.hash:
            if (value - num) in self.hash and (
                    value - num != num or self.hash[num] > 1):  #duplicat case
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)