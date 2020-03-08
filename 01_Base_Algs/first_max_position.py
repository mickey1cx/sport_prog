# https://stepik.org/lesson/307317/step/3?unit=289405

n = int(input())
numbers = input().split(' ')
max_num = 0
idx = 0
for i in range(n):
    current_number = int(numbers[i])
    if max_num < current_number:
        max_num = current_number
        idx = i + 1
print(idx)

# 6
# 7 1 4 1 6 1
# 1

# input()
# print(max(enumerate(map(int, input().split())), key=lambda x: x[1])[0] + 1)
