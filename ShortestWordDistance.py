'''
input: list of words, str1, str2
output: number(index distance between str1 and str2)

example:
["practice", "makes", "perfect", "coding", "makes"]
'practice' : 0
'coding': 3 
=> 3 

'makes':1,4
'coding':3
=> 1 

'makes':1,7
'coding':3,5,6
=> 1 

str1 != str2 
str1 and str2 in the list
'''

#O(n) 2 pointer
def shortestDistance1(words, word1,word2):
    p1=p2= float('inf')
    res = float('inf')
    for i,w in enumerate(words):
        if w == word1:
            p1 = i 
        if w == word2:
            p2 = i
        res = min(res,abs(p2-p1))
    return res






def shortestDistance(array, word1, word2):
    dic = {}
    for i in range(len(array)):
        if array[i] not in dic:
            dic[array[i]] = [i]
        else:
            dic[array[i]].append(i)
    res = len(array)
    for i in dic[word1]:
        for j in dic[word2]:
            if abs(i-j) < res:
                res = abs(i-j)
    return res


print(shortestDistance1(["practice", "makes", "perfect",
                        "coding", "makes"], 'coding', 'practice'))
print(shortestDistance1(["practice", "makes", "perfect",
                        "coding", "makes"], 'makes', 'coding'))
