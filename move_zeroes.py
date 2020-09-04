def moveZeros(nums):
    for j in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)


def moveZeros1(nums):
    count_zero = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                nums[j] = nums[i]
                j += 1

        k = len(nums) - 1
        while count_zero > 0:
            nums[k] = 0
            k -= 1
            count_zero -= 1


#All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.

#All elements between the current and slow pointer are zeroes.
def moveZeroes(nums):
    zero_idx = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1


# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

#zero_odx: 0,0,1,1
#i:0,1,2,3
#nums[i]:0,1,0,0
#[1,0,0,3,12]=>[1,3,]