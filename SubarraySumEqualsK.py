# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


#Brute Force
def subarraySum(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count


# Hash Table/sum(i,j)=sum(0,j)-sum(0,i)
def subarraySum1(nums, k):
    count = 0
    total = 0
    dic = {0: 1}
    for i in range(len(nums)):
        total += nums[i]
        if (total - k) in dic.keys():
            count += dic[total - k]
        if total not in dic:
            dic[total] = 1
        else:
            dic[total] += 1
    return count
