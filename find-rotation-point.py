words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
]

#Brute Force O(N)
def find_rotation_point(words):
    l = 0
    r = len(words)-1
    while l < r:
        print(l, r)
        mid = (r+l)//2 
        if words[mid][0] > words[l][0]:
            l = mid 
        else:
            r = mid 
        if r-l == 1:
            return r

             
print(find_rotation_point(words))
