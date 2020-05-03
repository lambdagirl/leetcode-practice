# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


#My initial solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic = {}
        for m in magazine:
            if m not in dic:
                dic[m] = 1
            else:
                dic[m] += 1
        for r in ransomNote:
            if r not in dic or dic[r] == 0:
                return False
            dic[r] -= 1

        return True


#improved solution
#Time Complexity : O(m)
#Creating a HashMap of counts for the magazine is O(m)O(m), as each insertion/ count update is is O(1)O(1), and is done for each of the mm characters.
#We then iterate over the ransom note, performing an O(1)O(1) operation for each character in it. This has a cost of O(n)O(n).
#Becuase we know that m ≥ nm≥n, again this simplifies to O(m)O(m).
import collections


def canConstruct(ransomNote, magazine):
    if len(magazine) < len(ransomNote): return False

    dic = collections.Counter(magazine)
    for r in ransomNote:
        if dic[r] <= 0: return False
        dic[r] -= 1
    return True
