import time

import flask


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

a = [1, 3]
b = [[1, 3], [3, 5], [1, 2]]

l = [1, 2, 3, 4, 5, 6]


print(a in b)
print(b.index(a))
print(b[b.index(a)])
b[1] = [1, 1]

l.remove(l[len(l) - 1])
for j in range(len(b)):
    print(b[j][0], b[j][1])

print(l)
