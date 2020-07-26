# A sorted array consisting of only integers 
# where every element appears exactly twice,
# except for one element which appears exactly once. 
# Find this single element that appears only once.


# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
# Input: [3,3,7,7,10,10,11,12,12]
# Output: 10

# Note: Your solution should run in O(log n) time and O(1) space.

# Approach 1: Brute Force; O(N); spaceO(1)
def singleNonDuplicate(nums):
    for i in range(0, len(nums)-2, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]

# Approach 2: Binary Search; O(logN); spaceO(1)
def singleNonDuplicate1(nums):
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == nums[mid - 1]:
            if (r-mid) % 2 == 0:
                r = mid - 2
            else:
                l = mid + 1
        elif nums[mid] == nums[mid + 1]:
            if (r-mid) % 2 == 0:
                l = mid + 2
            else:
                r = mid - 1
        else:
            return nums[mid]
    return nums[l]

#3 Binary Search on even index:

def singleNonDuplicate2(nums):
    l = 0
    r = len(nums) -1

    while l < r:
        mid = l + (r-l) //2
        if mid % 2 == 1:
            mid -=1
        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else:
            r = mid 
    return mid[l]