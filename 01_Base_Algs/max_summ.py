# https://stepik.org/lesson/307317/step/7?unit=289405

INF = pow(10, 9)
n = int(input())

num_sum = 0
sum_max = -INF - 1
sum_min = 0
# pref_sum = [0] * (n + 1)
for i, e in enumerate((int(x) for x in input().split())):
    num_sum += e
    # old code
    # pref_sum[i] = num_sum

    # https://e-maxx.ru/algo/maximum_average_segment
    sum_max = max(sum_max, num_sum - sum_min)
    sum_min = min(sum_min, num_sum)

# old code
# for l in range(n):
#     for r in range(l, n):
#         result = pref_sum[r + 1] - pref_sum[l]
#         if result > sum_max and not result == 0:
#             sum_max = result

print(sum_max)

# https://stepik.org/lesson/307317/step/7?discussion=1466909&thread=solutions&unit=289405
# from functools import reduce
#
# MIN = -10 ** 9
#
#
# def cummax(x, y):
#     x0, x1 = x
#     if x0 < 0:
#         return (y, max(x1, x0))
#     if y < 0:
#         x1 = max(x1, x0)
#     return (x0 + y, x1)
#
#
# n = input()
# print(max(reduce(cummax, map(int, input().split()), (MIN, MIN))))