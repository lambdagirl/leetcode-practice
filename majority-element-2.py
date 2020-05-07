# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

# Output will be either 1 number or 2 numbers
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.Counter()
        for num in nums:
            count[num] += 1
            if len(count) == 3:
                #This line is important
                count -= collections.Counter(set(count))
        return [k for k in count.keys() if nums.count(k) > len(nums) / 3]
