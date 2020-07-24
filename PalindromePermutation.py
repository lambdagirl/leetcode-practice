'''
"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

1. Brute Force: O(n!n)
2. rephrasing the problem:

civic
-   - 

civic
 _ _ 

civic
  _

* track if a character appears odd number 



'''

def has_palindrome_permutation(s):
    unpaired_char = set()
    for char in s:
        if char in unpaired_char:
            unpaired_char.remove(char)
        else:
            unpaired_char.add(char)
    return len(unpaired_char) <= 1


print(has_palindrome_permutation('livci'))
print(has_palindrome_permutation('ivicc'))
