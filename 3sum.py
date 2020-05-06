# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(nums):
    nums.sort()  #O(N)
    res = []
    for i, num in enumerate(nums):
      # avoid duplicate for the first num in the triplets
        if i == 0 or nums[i-1] != [nums[i]]:
          l = i + 1
          r = len(nums) - 1
          total = num + nums[l] + nums[r]
          while l < r:
              # avoid duplicate for the second num in the triplets
              if total < 0 or (nums[l] == nums[l-1] and l > i + 1)
                  l += 1
             # avoid duplicate for the third num in the triplets
              elif total > 0 or (nums[r] == nums[r + 1] and r < len(nums) - 1 ):
                  r -= 1
              else:
                  res.append([num, nums[l], nums[r]])
                  l += 1
                  r -= 1
      return res
            
