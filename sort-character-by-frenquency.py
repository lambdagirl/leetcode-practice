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


def frequencySort(s):
    res = ""
    dic = collections.Counter(s)
    for k, v in sorted(dic.items(), key=lambda kv: kv[1], reverse=True):
        res += k*v
    return res


def frequencySort_oN(s):
    counts = collections.Counter(s)
    max_freq = max(counts.values())
    buckets = [[] for _ in range(max_freq + 1)]
    for k, v in counts.items():
        buckets[v].append(k)
    res_list = []

    for i in range(len(buckets) - 1, 0, -1):
        for letter in buckets[i]:
            res_list.append(i*letter)
    return ''.join(res_list)


print(frequencySort("tree"))
print(frequencySort_oN("tree"))
