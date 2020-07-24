'''
32-bit signed integer => -2^31 < n < 2^31-1

examples:
123 => 321
['1','2','3'] => ['3','2','1'] => 321

-123 => -321 
 ['-','1','2','3']=> ['-','3','2','1'] 

1200 => 21

['1','2',']
9 => 9
-9 => -9

overflows => 0 

1.split str to list=>  reverse list (2 pointers)=> join
2.num//10...100...1000 => 
'''

# def reverse(num):
#     ans = 0
#     for i in range(1,len(str(num))+1):
#         ans += num % (pow(10,i))
#         num = num // (pow(10, i))
#         print(num)
#     return ans



def reverse(num):
    arr = list(str(num))
    l = 0
    if num < 0:
        l = 1
    r = len(arr)-1
    while l < r:
        if l >= r:
            break
        arr[l], arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    res = int(''.join(arr))
    if res <= -pow(2, 31) or res > pow(2, 31)-1:
        return 0
    return res


print(reverse(123))
print(reverse(-123))
print(reverse(10200))
