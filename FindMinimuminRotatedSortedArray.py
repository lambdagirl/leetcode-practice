
# Example 1:

# Input: [3, 4, 5, 1, 2]
# Output: 1
# Example 2:

# Input: [4, 5, 6, 7, 3]
# Output: 3


# Input: [6,1,2,3,4,5]
# Output: 1


# A very brute way of solving this question is to search the entire array and find the minimum element. The time complexity for that would be O(N)O(N) given that N is the size of the array.
def findMin(nums):
    l = 0
    r = len(nums) -1

    if nums[r] >= nums[l]:
        return nums[l]
    
    while l +1 < r:
        mid = l + (r-l) //2
        if nums[mid] > nums[l]:
            l = mid
        else:
            r = mid
    return nums[r]


# If a sorted array is shifted, if you take the middle, if middle is less than [right] (last), then minimum will be on the left side, otherwise it will be on the right side.
def findMin2(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = l + (r-l) // 2
        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid +1
    return nums[l]


print(findMin([6, 2, 3, 4, 5]))
