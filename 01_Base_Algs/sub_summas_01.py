# https://stepik.org/lesson/307317/step/6?unit=289405

import sys

user_input = sys.stdin.readline     # for fast input

params = user_input().split()
n, q = map(int, params)

num_sum = 0
pref_sum = [0] * (n + 1)
for i, e in enumerate((int(x) for x in user_input().split()), start=1):
    num_sum += e
    pref_sum[i] = num_sum

result = [0] * q
for i in range(q):
    params = user_input().split()
    l, r = map(int, params)
    result[i] = pref_sum[r] - pref_sum[l - 1]

print(*result, sep='\n')

# https://stepik.org/lesson/307317/step/6?discussion=1466813&thread=solutions&unit=289405
# from sys import stdin
# from itertools import accumulate, starmap
#
# reader = (map(int, line.split()) for line in stdin)
# n, q = next(reader)
# sums = list(accumulate(next(reader)))
# sums.append(0)
# print(*starmap(lambda i, j: sums[j-1] - sums[i-2], reader), sep='\n')