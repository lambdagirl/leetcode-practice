matrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
#[[1,0,0],[0,1,0],[1,1,1]]
def flipAndInvertImage(matrix):
    ans = []
    for r in matrix:
        new_r=[]
        r = r[::-1]
        for num in r:
            new_r.append(num ^ 1)
        ans.append(new_r)
    return ans

print(flipAndInvertImage(matrix))
