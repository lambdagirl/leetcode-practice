# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false
#bianry search
'''
x * x = 16 => True
the square root aa is always less than extrm{num} / 2num/2 and greater than 1:
'''
def isPerfectSquare(num):
    if num == 1:
        return True
    l, r = 2, num // 2
    while l <= r:
        mid = l + (r-l) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return False
    
print(isPerfectSquare(2))
