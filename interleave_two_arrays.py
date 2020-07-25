'''
input: (list, list)
output: list

example: 
1.['a','c','s'],['a','b','x'] => ['a','a','c','b','s','x']
1.['a','c','s'],['a','b','x','x','z'] => ['a','a','c','b','s','x','x','z]?



'''
#same length:
#basic soltion 
def interleave(array1,array2):
    array3 =[] 
    for i in range(len(array1)):
        array3.append(array1[i])
        array3.append(array2[i])
    return array3

#save some space, merge to array1
def interleave1(array1, array2):
    for i in range(len(array2)):
        array1.insert(2*i+1,array2[i])
    return array1

print(interleave1(['a', 'c', 's','z'], ['a', 'b', 'x']))

#different length 2 array

def interleave3(array1, array2):
    min_length = min(len(array1),len(array2))
    array3 = []
    for i in range(min_length):
        array3.append(array1[i])
        array3.append(array2[i])
    if len(array1)> min_length:
        array3 += array1[i:]
    else: 
        array3 += array2[:i]
    return array3

print(interleave3(['a', 'c', 's', 'z','s'], ['a', 'b', 'x']))


#different length n array
'''
[['a','b','c'],
['d','e','f','g','h'],
['i','j','k'],
['l','m','n','o']]

=>
['a','d','i','l','b','e','j','m','c','f','k','n','g','o','h']

'''
def interleaveArrays(lists):
    res = []
    i = 0
    done = False
    while not done:
        done = True
        for l in lists:
            if i < len(l):
                res.append(l[i])
                done = False
        i +=1
    return res

print(interleaveArrays([[1,2,3],['a','b','c','d','r']]))
