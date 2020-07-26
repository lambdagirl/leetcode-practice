"""
n is always non negative (n >= 0)
0 <= n <= 2^31 -1
n = 10 
Should return 4

-
-- 
--- 
---- 

n = 12
Should return 4
-
-- 
--- 
---- 
-- (not full)

n = 0
Return return 0

n = 1
Should return 1

#########

To form X rows

(1 + 2 + 3 + ... + X) <= n => (1+X)*X//2 <=n

########

n = 0

r = 2
c = 3


* 
** 
***
****
*****

l = [1,2,3,4,5]
sum(l) = (l[0]+l[-1])*len(l)//2 < n


"""

def arrangeCoins(n):
        row = 0
        counter = 1
        while n >= counter:
            n -= counter
            row += 1
            counter += 1
        return row

def arrangeCoins1(n):
    l = 0
    r = n 
    while l <= r:
        x = (r+l)//2
        curr = x * (x+1)//2
        if curr == n:
            return x
        if n < curr:
            r = x-1
        else:
            l = x+1
    return r
