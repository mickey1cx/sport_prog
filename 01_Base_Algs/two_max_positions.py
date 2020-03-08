# https://stepik.org/lesson/307317/step/4?unit=289405


def NextRand(cur, a, b):
    return (cur * a + b) % 1791791791


#n = int(input())                    # 4             # 4
#numbers = input().split(' ')        # 2 2 2         # 113179 179113 113113

# current_number = int(numbers[0])
# a = int(numbers[1])
# b = int(numbers[2])
arr = [6, 14, 35, 27, 30, 20, 30, 25, 35]                            # 6 14 30 62    # 562233639 1071657538 309314241 1791375417
n = len(arr)

# for i in range(n):
#     next_rand = NextRand(current_number, a, b)
#     arr.append(next_rand)
#     current_number = next_rand

max_a = 0
max_b = 0
idx_a = 0
idx_b = 0
for i in range(n):
#    current_number = NextRand(current_number, a, b)
    current_number = arr[i]
    if max_a < current_number:
        max_b = max_a
        max_a = current_number
        idx_b = idx_a
        idx_a = i
    elif max_b < current_number:
        max_b = current_number
        idx_b = i

#print(*arr)
print(idx_a + 1, idx_b + 1)
