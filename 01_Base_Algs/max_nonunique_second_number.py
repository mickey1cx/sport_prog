# https://stepik.org/lesson/307317/step/1?unit=289405
# find non unique second max number

import random as r
max_n = 10000000
max_value = 100000000
r.seed(0)   # for re-use

n = max(2, min(int(input('Nums count: ')), max_n))
a = []
for i in range(n - 1):
    a.append(r.randint(0, max_value))
a.insert(int(len(a) / 2), max(a))    # double max value

max_a = 0
max_b = 0
for i in range(n):
    if max_a < a[i]:
        max_b = max_a
        max_a = a[i]
    elif max_b <= a[i]:
        max_b = a[i]

print(*a)
print(max_a)
print(max_b)

# for test, built-in funcs
a.sort()
print(*a)

