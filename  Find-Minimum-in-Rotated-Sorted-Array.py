
# Example 1:

# Input: [3, 4, 5, 1, 2]
# Output: 1
# Example 2:

# Input: [4, 5, 6, 7, 0, 1, 2]
# Output: 0
def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        if len(nums) ==1:
            return nums[0]
        
        if nums[r] > nums[l]:
            return nums[l]
        
        while l < r:
            mid = (l + r) //2
            if nums[mid] > nums[l]:
                l = mid
            elif nums[mid] < nums[l]:
                r = mid
            if r - l == 1:
                return nums[r]
