'''
input: list[int], rotated, int may contain duplicates.
output: minimum int


input [4,5,1,2] => [1,2,4,5] => output: 1 
input [2,2,2,0,1] => [0,1,2,2,2] => output: 0
input [2,3,3,1,1] => [1,1,2,3,3] => output: 1

[2,2,2,1,2]
1.O(N) min(list)
2.find the rotation point: binary search log(N).

'''

def findMin(nums):
    l = 0
    r = len(nums)-1 
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] < nums[r]:
            r = mid
        elif nums[mid] > nums[l]:
            l = mid +1
        else:
            r-=1
    return nums[l]
print(findMin([4, 5, 1, 2]))

