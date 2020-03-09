# https://stepik.org/lesson/307317/step/8?unit=289405

from collections import Counter

year = int(input())
max_year = 10**9
result = -1

while year < max_year:
    year += 1
    digits = Counter(map(int, str(year)))
    err = False
    for number, count in digits.items():
        if number == 0 or number == 2:
            err = True
            break
        elif count > 1:
            err = True
            break
    if not err:
        result = year
        break

print(result)
