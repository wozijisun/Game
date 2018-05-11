import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

a = [1, 4]
b = [[1, 3], [3, 5], [1, 2]]

print(a in b)
print(b.index(a))
print(b[b.index(a)])

for j in range(len(b)):
    print(b[j][0], b[j][1])
