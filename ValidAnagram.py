'''
input: string: s,t (lowercase)
output: Boolean

example:
s = "anagram", t = "nagaram"
=> True

=> False

'''
s = "ab"
t = "a"


import collections
def Anagram(s,t):
    dic = collections.Counter(s)
    for char in t:
        if char not in dic or dic[char] <= 0:
            return False 
        dic[char] -=1
    print(dic)
    return sum(dic.values()) == 0

print(Anagram(s, t))
