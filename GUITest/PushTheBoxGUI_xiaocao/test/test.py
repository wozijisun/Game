import time



print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

a = [1, 3]
b = ['[1, 3]', '[3, 5]', '[1, 2]']
b.remove('[1, 3]')
print(b)
