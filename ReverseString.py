# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


#Will not work, O(N) space complexity
def reverseString1(s):
    if len(s) == 0:
        return s
    else:
        return reverseString1(s[1:]) + [s[0]]


#O(1) space complexity
def reverseString(s):
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)


s = ["H", "a", "n", "n", "a", "h"]
reverseString(s)
print(s)

#O(logN) two pointers
def reverse(strs):
    left_idx = 0
    right_idx = len(strs)-1

    while left_idx < right_idx:
        strs[left_idx], strs[right_idx] = strs[right_idx], strs[left_idx]
        left_idx +=1
        right_idx -=1

