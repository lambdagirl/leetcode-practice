# Example:

# Input:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [0, 5, 6],       n = 3

# Output: [1, 2, 2, 3, 5, 6]

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is equal to m + n) to hold additional elements from nums2.

# Constraints:

# -10 ^ 9 <= nums1[i], nums2[i] <= 10 ^ 9
# nums1.length == m + n
# nums2.length == n

# Approach : Two pointers / Start from the end
# O(M+N)
def merge(nums1,nums2,m,n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        #case nums2 still have n element left
        nums1[:n] = nums2[:n]

#Approach: Merge and Sort
def merge_and_sort(nums1,nums2,m,n):
    nums1 = nums1[:m] + nums2 
    sorted(nums1)
