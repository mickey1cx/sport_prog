# https://stepik.org/lesson/307317/step/1?unit=289405
# find max number

import random as r
max_n = 10000000
max_value = 100000000

n = int(input('Nums count: '))
a = []
for i in range(n):
    a.append(r.randint(0, max_value))

max_a = 0
for i in range(n):
    if max_a < a[i]:
        max_a = a[i]

print(*a)
print(max_a)

# for test, built-in funcs
print(max(a))
a.sort()
print(*a)

