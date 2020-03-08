# https://stepik.org/lesson/307317/step/5?unit=289405

import random as rnd

rnd.seed(0)
n = 20
q = rnd.randint(10, n)

nums = [0]
nums_sum = 0
for i in range(n):
    num = rnd.randint(0, n)
    nums_sum += num
    nums.append(nums_sum)

for i in range(q):
    l = rnd.randint(1, int(n / 2))
    r = rnd.randint(l, n)
    print(l, r, nums[r] - nums[l])

print(*nums)
