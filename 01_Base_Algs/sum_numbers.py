# https://stepik.org/lesson/307317/step/2?unit=289405

sum_numbers = 0
n = int(input())
numbers = input().split(' ')
for i in range(n):
    sum_numbers += int(numbers[i])
print(sum_numbers)

# 6
# 1 3 4 3 5 4
# 20

# input()
# print(sum(map(int, input().split())))