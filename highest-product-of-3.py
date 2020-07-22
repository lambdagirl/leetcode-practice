
# Given a list of integers, find the highest product you can get from three of the integers.

# The input list_of_ints will always have at least three integers.

# input: all positive [1,2,3,4,2] =>  [2*3*4] => output:24

# input [-2,-3, 2, 4] => [-2,-3,4] => 24
# input [-2,-3,-2, -1] => [-2,-2,-1]
# input [-2,-3,-2, 1] => [-2,-3,1]

#nlog(n)
def highest_product_of_3_1(list_of_ints):
    list_of_ints.sort()
    return max(list_of_ints[-1]*list_of_ints[-2]*list_of_ints[-3], list_of_ints[0]* list_of_ints[1]* list_of_ints[-1])

# def highest_product_of_3(list_of_ints):
#     num1, num2, num3 = list_of_ints[0], list_of_ints[1], list_of_ints[2]
#     max_output = num1*num2*num3
#     temp_num = min(num1,num2,num3)
#     if len(list_of_ints) == 3:
#         return max_output
# 
#     for num in list_of_ints[3:]:
#         if num > min(num1, num2, num3):
#             temp_num = num

list_of_ints = [-1, 2, 3, -4]
print(highest_product_of_3_1(list_of_ints))
