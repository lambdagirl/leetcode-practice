# # 451. Sort Characters By Frequency
# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        res = ""
        for k, v in (sorted(dic.items(), key=lambda kv: kv[1], reverse=True)):
            res += k*v
        return res


print(frequencySort("tree"))
