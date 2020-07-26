'''
input: integer >= 0
output: integer 
(repeatedly add all its digits until the result has only one digit.) 

exple: 
38 => 3+8 => 11 => 1+1 => 2

9 => 9
'''
def addDigits(num):
    if num < 10:
        return num 
    num = num//10 + num % 10
    return addDigits(num)
print(addDigits(28))


def addDigits1(num):
    while len(str(num)) > 1:
        num = sum([int(n) for n in str(num)])
    return num
