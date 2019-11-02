def LCS(v, w):    
    s = [[x + y for x in range(len(v) + 1)] for y in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, len(v) + 1):
            if v[j - 1] == w[i - 1]:
                s[i][j] = s[i - 1][j - 1]
            else:
                s[i][j] = min([s[i - 1][j], s[i][j - 1], s[i - 1][j - 1]]) + 1
    return s[-1][-1]

with open('input.txt') as file:
    w = file.readline().strip()
    v = file.readline().strip()

s = LCS(w, v)
print(s)