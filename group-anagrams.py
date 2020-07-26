# 49. Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

#klogk * n
def groupAnagrams(strs):
    dic = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in dic: 
            dic[key] = [s]
        dic[key].append(s)
    return list(dic.values())


#k * n
def groupAnagrams1(strs):
    dic = {}
    for s in strs:
        count = [0] * 26
        for l in s:
            count[ord(l) - ord('a')] +=1
        if tuple(count) not in dic:
            dic[tuple(count)] = [s]
        else:
            dic[tuple(count)].append(s)
    return dic.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams1(strs))
