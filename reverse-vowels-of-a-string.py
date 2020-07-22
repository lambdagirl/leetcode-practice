# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

#Solution1 O(N)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        #'hello' => 'eo'=> 'holle'
        #'leetcode' => 'eeoe' => 'leotcede'
        reverse = []
        for i in range(len(s)):
            if s[i] in vowels:
                reverse.append(s[i])
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + reverse.pop() + s[i+1:]
        return s

#Solution2 log(N)
#two pointers

def reverseVowels(s):
    vows = 'aeiouAEIOU'
    l, r = 0, len(s) - 1
    s = list(s)
    while l < r:
        if s[l] not in vows:
            l += 1
            continue
        if s[r] not in vows:
            i -=1
            continue

        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)


